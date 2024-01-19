from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Max
import json

from .models import User, Flashcard, Stats, Proficiency


@login_required
def new_flashcard(request):
    if request.method == "POST":
        english_word = request.POST["english-word"]
        translation = request.POST["translation"]
        flashcard_img = request.FILES["flashcard-img"]

        # Attempt to create new flashcard
        try:
            flashcard = Flashcard.objects.create(english_word=english_word, translation=translation, image=flashcard_img)
            flashcard.save()
        except IntegrityError:
            return render(request, "flashcards/new_flashcard.html", {
                "message": "Flashcard already exists with the same word."
            })
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "flashcards/new_flashcard.html")

@login_required
def set_proficiency(request):
    """Updates user proficiency of a word"""
    #the request method is checked to make sure it is a POST request
    if request.method == "POST":
        #the request body is accessed using request.body, which contains the raw request payload
        data = request.body
        # data is a bytes-like object, so you might want to convert it to a dictionary or a string
        data = data.decode('utf-8')
        # parse the JSON data
        data = json.loads(data)
        # now you can access the data as a dictionary
        proficiency = data['proficiency']
        card_id = data['card_id']
        flashcard = Flashcard.objects.get(pk=card_id)

        try:
            # Si existe, actualizarlo. Sino, crearlo
            if Proficiency.objects.filter(user=request.user, flashcard=flashcard).exists():
                prof_obj = Proficiency.objects.get(user=request.user, flashcard=flashcard)
                prof_obj.level = proficiency
                prof_obj.last_studied = timezone.now
                prof_obj.save()
            else:
                Proficiency.objects.create(user=request.user, flashcard=flashcard, level=proficiency, last_studied=timezone.now)
            
            update_stats(request)
            if proficiency == 1:
                return JsonResponse({'message': f'You learned a new word: {flashcard.english_word}', 'result': 'success'},safe=False)
            elif proficiency == 0:
                return JsonResponse({'message': f'You need to practice more: {flashcard.english_word}', 'result': 'success'},safe=False)
        except Flashcard.DoesNotExist:
            return JsonResponse({'error': f'The flashcard with id {card_id} does not exist', 'result': 'error'}, status=400)
        
    else:
        return JsonResponse({'error': 'Bad request', 'result': 'error'}, status=400)
    

@login_required
def update_stats(request):
    """Calculates and returns the user's statistics."""
    total_cards = Proficiency.objects.filter(user=request.user).count()
    need_practice_cards = Proficiency.objects.filter(user=request.user, level=0).count()
    learned_cards = Proficiency.objects.filter(user=request.user, level=1).count()
    if total_cards == 0:
        percent_learned = 100
    else:
        percent_learned = (learned_cards / total_cards) * 100

    # Update stats in database
    s = Stats.objects.get(user=request.user)
    s.total_cards=total_cards
    s.need_practice_cards=need_practice_cards
    s.learned_cards=learned_cards
    s.percent_learned=percent_learned
    s.last_studied=timezone.now()
    s.save()


def index(request):
    return render(request, "flashcards/index.html",)


@login_required
def study(request):
    # Get all new flashcards 
    flashcards_to_study = Flashcard.objects.exclude(
        pk__in=Proficiency.objects.filter(
            user=request.user
        ).values_list('flashcard__id', flat=True)
    ).order_by('-pk')[:10]

    paginator = Paginator(flashcards_to_study, 1) # Show 1 flashcard per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_card=None
    if len(page_obj) > 0:
        current_card = page_obj[0]

    return render(request, "flashcards/study.html", {
        'page_obj': page_obj,
        'card': current_card
    })


@login_required
def review(request):
    # Get flashcards to review
    flashcards_to_review = Flashcard.objects.filter(
        pk__in=Proficiency.objects.filter(
            user=request.user,
            level=0
        ).values_list('flashcard__id', flat=True),
        # Append last studied field to flashcards?
        
    ).order_by('-pk')[:10]

    paginator = Paginator(flashcards_to_review, 1) # Show 1 flashcard per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_card=None
    if len(page_obj) > 0:
        current_card = page_obj[0]

    return render(request, "flashcards/review.html", {
        'page_obj': page_obj,
        'card': current_card
    })


@login_required
def learned(request):
    # Get count of learned words
    stats = Stats.objects.get(user=request.user)
    card_count=stats.learned_cards
    
    # Get set of learned flashcards
    learned_cards = Flashcard.objects.filter(
        pk__in=Proficiency.objects.filter(
            user=request.user,
            level=1
        ).values_list('flashcard__id', flat=True)
    ).annotate(last_studied=Max('proficiency__last_studied')).order_by('-last_studied')

    paginator = Paginator(learned_cards, 10) # Show 10 learned flashcards per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    return render(request, "flashcards/learned.html", {
        'card_count': card_count,
        'page_obj': page_obj,
    })


@login_required
def profile(request):
    # update_stats(request)
    stats = Stats.objects.get(user=request.user)

    return render(request, "flashcards/stats.html", {
        'stats': stats
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "flashcards/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "flashcards/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        profile_pic = request.FILES.get("profile_pic")

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "flashcards/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, profile_pic=profile_pic)
            user.save()

            # Create user first stats
            stats = Stats.objects.create(user=user)
            stats.save()
        except IntegrityError:
            return render(request, "flashcards/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "flashcards/register.html")
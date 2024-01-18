from django.contrib import admin
from flashcards.models import User, Flashcard, Stats, Proficiency

# Register your models here.
admin.site.register(User)
admin.site.register(Flashcard)
admin.site.register(Stats)
admin.site.register(Proficiency)
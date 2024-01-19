from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.utils import timezone


def flashcard_image_src(instance, filename):
    return 'img/flashcards/' + instance.english_word + '.jpg'


def profile_pic_src(instance, filename):
    return 'img/users/' + instance.username + '.jpg'


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to=profile_pic_src, default='img/users/default.jpg', null=True, blank=True) 

    def __str__(self):
        return f"{self.username}"
    
class Flashcard(models.Model):
    english_word = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=flashcard_image_src, default='img/flashcards/default.jpg') 
    translation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.english_word} means {self.translation}"

class Proficiency(models.Model):
    CHOICES = [(0,'Need Practice'),(1,'Learned')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    level = models.IntegerField(choices=CHOICES)
    last_studied = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'flashcard',)

    def __str__(self):
        return f"{self.flashcard} - {self.level}"

class Stats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_cards = models.IntegerField(default=0)
    need_practice_cards = models.IntegerField(default=0)
    learned_cards = models.IntegerField(default=0)
    percent_learned = models.DecimalField(default=100.00, max_digits=5, decimal_places=2)
    last_studied = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} has studied {self.total_cards} flashcards, of which {self.learned_cards} have been learned"
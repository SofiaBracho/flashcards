from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("study", views.study, name="study"),
    path("review", views.review, name="review"),
    path("learned", views.learned, name="learned"),
    path("profile", views.profile, name="profile"),
    path("set_proficiency", views.set_proficiency, name="set_proficiency"),
]
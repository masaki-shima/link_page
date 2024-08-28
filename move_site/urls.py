from django.urls import path

from . import views

app_name = "move_site"
urlpatterns = [
    path("", views.movesite, name="index"),
    path("scroll/", views.scroll, name="scroll"),
    path("scroll_animation/", views.scroll_animation, name="scroll_animation"),
    path("bootstrap/", views.bootstrap, name="bootstrap"),
]

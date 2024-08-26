from django.urls import path

from . import views

app_name = "move_site"
urlpatterns = [
    path("", views.movesite, name="index"),
]

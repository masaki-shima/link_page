from blog.views import frontpage, post_detail
from django.urls import path

app_name = "blog"
urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("<slug:slug>/", post_detail, name="post_detail"),
]

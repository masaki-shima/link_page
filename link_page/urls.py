from django.urls import path

from . import views

app_name = "link_page"
urlpatterns = [
    path("", views.index, name="index"),
    path("page/create/", views.page_create, name="page_create"),
    path("comment/", views.comment_list, name="comment_list"),
    path("comment/<uuid:id>/", views.comment_detail, name="comment_detail"),
    path("comment/<uuid:id>/update/", views.comment_update, name="comment_update"),
    path("comment/<uuid:id>/delete/", views.comment_delete, name="comment_delete"),

    # DBを使わないページ
    path("dropdown00/", views.DropdownView00.as_view(), name="dropdown00"),
    path("dropdown01/", views.DropdownView01.as_view(), name="dropdown01"),
    path("jquery/", views.jQueryView.as_view(), name="jquery"),
    path("test/", views.TestView.as_view(), name="test"),
]

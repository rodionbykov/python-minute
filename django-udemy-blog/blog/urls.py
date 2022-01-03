from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.details, name="post-details-page")
]

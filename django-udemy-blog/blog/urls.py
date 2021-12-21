from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("posts", views.posts),
    path("posts/<slug:slug>", views.detail, name="post-detail-page")
]

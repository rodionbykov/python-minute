from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartPageView.as_view(), name="index"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SingleView.as_view(), name="post-details-page")
]

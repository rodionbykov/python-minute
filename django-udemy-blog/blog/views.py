from datetime import date

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm

# Create your views here.


class StartPageView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class SingleView(DetailView):
    template_name = "blog/details.html"
    model = Post # will search by primary key automatically

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context


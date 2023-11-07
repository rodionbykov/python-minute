from datetime import date

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
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

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }

        return render(request, "blog/details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm()
        }

        return render(request, "blog/details.html", context)


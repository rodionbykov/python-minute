from datetime import date

from django.shortcuts import get_object_or_404, render
from django.views.generic import View, ListView, DetailView
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

        saved_posts = request.session.get("saved_posts")

        if saved_posts is not None:
            is_saved_post = post.id in saved_posts
        else:
            is_saved_post = False

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "is_saved_post": is_saved_post
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


class ReadLaterView(View):

    def get(self, request):

        saved_posts = request.session.get("saved_posts")

        context = {}

        if saved_posts is None or len(saved_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = Post.objects.filter(id__in=saved_posts)
            context["has_posts"] = True

        return render(request, "blog/saved.html", context)

    def post(self, request):

        saved_posts = request.session.get("saved_posts")

        if saved_posts is None:
            saved_posts = []

        post_id = int(request.POST["postid"])

        if post_id not in saved_posts:
            saved_posts.append(post_id)

        request.session["saved_posts"] = saved_posts

        return HttpResponseRedirect("/")

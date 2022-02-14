from datetime import date

from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.

def index(request):
    arr_posts = Post.objects.all().order_by("-date")[:3] # sql will be properly generated!
    return render(request, "blog/index.html", {
        "posts": arr_posts
    })

def posts(request):
    arr_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": arr_posts
    })

def details(request, slug):
    the_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/details.html", {
        "post": the_post,
        "post_tags": the_post.tags.all()
    })

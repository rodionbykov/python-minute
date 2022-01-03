from datetime import date

from django.shortcuts import render

arr_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Sam Frodo",
        "date": date(2021, 12, 30),
        "title": "Hiking in the mountains",
        "excerpt": "Aliquam erat volutpat. Curabitur dignissim a sem eu interdum. Vivamus fermentum euismod pulvinar.",
        "content": """
            Aenean vel ipsum ac nibh congue luctus. 
            Sed hendrerit consequat metus ac sagittis. Donec ac risus molestie, condimentum sem sit amet, lobortis eros. Nulla facilisi. Aliquam fermentum pellentesque nunc quis fermentum. Nullam justo augue, viverra sed enim quis, placerat efficitur augue. Aliquam volutpat euismod sapien, quis dignissim purus pharetra vitae. Ut molestie nisi at ultrices aliquam. 
            Aliquam erat volutpat. Nullam at metus ante. Nam sed maximus sapien, semper consectetur nisi. Sed et accumsan elit. Donec auctor libero eu porttitor viverra. Duis quis eros vitae mi congue pretium at eget nibh. Mauris sed odio sit amet sem luctus pellentesque. Nam faucibus, neque vitae eleifend ultricies, elit felis aliquam nibh, sed sodales sem felis ut dolor.
        """
    }
]

# Create your views here.

def index(request):
    return render(request, "blog/index.html", {
        "posts": arr_posts
    })

def posts(request):
    return render(request, "blog/posts.html", {
        "posts": arr_posts
    })

def details(request, slug):
    the_post = next(post for post in arr_posts if post['slug'] == slug)
    return render(request, "blog/details.html", {
        "post": the_post
    })

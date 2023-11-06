from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=127)
    email = models.EmailField(max_length=127, null=True)
    
    def __str__(self):
        return f"{self.full_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=31)

    def __str__(self):
        return f"{self.caption}"
    
    
class Post(models.Model):
    title = models.CharField(max_length=127)
    excerpt = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(20)])
    likes = models.IntegerField(validators=[MinValueValidator(0)])
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=127)
    user_email = models.EmailField()
    body = models.TextField(max_length=511)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
from pyexpat import model
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=127)

class Post(models.Model):
    title = models.CharField(max_length=255)
    likes = models.IntegerField(validators=[MinValueValidator(0)])
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"{self.title}, {self.likes} likes"

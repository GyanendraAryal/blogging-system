from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    STATUS_CHOICES = [
        ("Draft", "DRAFT"),
        ("Published", "PUBLISHED"),
    ]
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to="uploads/%Y/%m/%d")
    short_description = models.TextField()
    blog_body = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default="Draft", max_length=20)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

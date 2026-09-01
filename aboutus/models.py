from django.db import models


# Create your models here.
class About(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.title


class SocialLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    platform = models.CharField(max_length=20)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform

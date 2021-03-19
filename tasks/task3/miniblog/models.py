from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    theme = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    data = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='post_photo/', null=True, blank=True)

    def __str__(self):
        return self.theme


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)



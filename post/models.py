from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=100)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)

    # This receiver handles token creation immediately a new user is created.
    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

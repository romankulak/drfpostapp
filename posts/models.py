from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def like_toggle(self, user, post_obj):
        if user in post_obj.liked.all():
            is_liked = False
            post_obj.liked.remove(user)
        else:
            is_liked = True
            post_obj.liked.add(user)
        return is_liked


class Post(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
    liked = models.ManyToManyField(
        'auth.User', blank=True, related_name='liked')

    objects = PostManager()

    def __str__(self):
        return self.content


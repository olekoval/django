from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    # дата та время публікації поста
    publish = models.DataTimeField(default=timezone.now)
    # дата та время створення поста
    created = models.DataTimeField(auto_now_add=True)
    # дата та время останнього оновлення поста
    updated = models.DataTimeField(auto_now=True)

    def __str__(self):
        return self.title

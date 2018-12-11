from django.db import models


class Category(models.Model):
    name =  models.CharField(max_length=40, unique=True)
    slug = models.SlugField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


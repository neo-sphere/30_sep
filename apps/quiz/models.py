from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name =  models.CharField(max_length=40, unique=True)
    slug = models.SlugField(blank=True, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name

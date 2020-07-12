from django.db import models
import random
import string
# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Urls(models.Model):

    def __str__(self):
        return self.redirect

    slug = models.CharField(max_length=6, unique=True, default=rand_slug())
    redirect = models.URLField(max_length=255, unique=False)

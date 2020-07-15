from django.db import models
from django.conf import settings
import random
import string
from randomslugfield import RandomSlugField


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Urls(models.Model):

    def __str__(self):
        return self.redirect

    slug = RandomSlugField(length=6)
    redirect = models.URLField(max_length=255, unique=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              null=True,
                              default=None)
    hits = models.IntegerField(default=0)

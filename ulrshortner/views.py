from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import models


# Create your views here.


def displayShortUrl(request, title):

    response = models.Urls.objects.filter(slug=title).values()

    if not response:
        return HttpResponse("No match found.")

    else:
        redirectURL = response[0]["redirect"]
        slug = response[0]["slug"]

        if title == slug:
            return redirect(redirectURL)

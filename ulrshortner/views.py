from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics
from . import models, serializer


# Create your views here.


def displayShortUrl(request, title):

    response = models.Urls.objects.filter(slug=title).values()
    response_queryset = models.Urls.objects.get(slug=title)

    if not response:
        return HttpResponse("No match found.")

    elif title == response[0]["slug"]:
        # On incrémente de 1 le compte de vue sur la page
        hits_count = response[0]["hits"] + 1
        response_queryset.hits = hits_count
        response_queryset.save()

        # On redirige vers la page choisie
        redirectURL = response[0]["redirect"]
        return redirect(redirectURL)


"""
POST request to create a short URL:

    Only need to provide in data: 
        - redirect = <yourURL>
    Need to provide in header your auth token to populate owner field (otherwise null):
        - Authorization = Token 8a2ec25b5931ab408c254e5cf0ec72b174062fc6

GET request to list all your short URLs created - If user is not authenticated, returns nothing
"""


class UrlList(generics.ListCreateAPIView):
    serializer_class = serializer.UrlSerializer

    def get_queryset(self):
        current_user = self.request.user
        if self.request.user.is_anonymous:
            return models.Urls.objects.none()
        else:
            return models.Urls.objects.all().filter(owner=current_user.id)

    def perform_create(self, serializer):
        if not self.request.user.is_anonymous:
            serializer.save(owner=self.request.user)
        else:
            serializer.save(owner=None)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import authenticate
from . import serializer
from django.contrib.auth.models import User


"""
This is the login method
POST Request only with username and password required fields
"""


@csrf_exempt
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


"""
This is the signup method
POST Request only with username and password required fields
"""


@csrf_exempt
@api_view(["POST"])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username)
        user.set_password(password)
        user.save()
    except Exception as error:
        return Response({'Status': 'ERROR: ' + str(error)})

    return Response({'Status': 'User created successfully'}, status=HTTP_200_OK)


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

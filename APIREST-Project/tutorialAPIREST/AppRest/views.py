from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serielizer import user_serializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = user_serializer

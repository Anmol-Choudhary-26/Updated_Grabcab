from django.shortcuts import render
from .models import User, Car
from .serializers import CarSerializer, UserSerializer
from rest_framework import viewsets


class UserviewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class CarviewSet(viewsets.ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer

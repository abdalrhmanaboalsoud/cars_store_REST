from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
from rest_framework.views import APIView

# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


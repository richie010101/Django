from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Ejemplo
from .serial import EjemploSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

class EjemploLista(generics.ListCreateAPIView):
    queryset = Ejemplo.objects.all()
    serializer_class = EjemploSerializer

class EjemploDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ejemplo.objects.all()
    serializer_class = EjemploSerializer

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})
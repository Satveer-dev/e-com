from django.shortcuts import render

from .models import Product
from .seriliazers import ProductSeriliazer
from rest_framework import viewsets

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeriliazer

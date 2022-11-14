from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions,authentication


from django.contrib.auth.models import User
from api.serializers import ProductsSerializer
from api.models import Products
# Create your views here.

class ProductsView(ModelViewSet):

    serializer_class=ProductsSerializer
    queryset=Products.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]
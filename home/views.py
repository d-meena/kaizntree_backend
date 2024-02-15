from django.shortcuts import render, HttpResponse
from django.urls import path
from home import views
from home.models import*
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework import viewsets
import json
from home.serializers import ProductSerializer, TagSerializer
from django_filters.rest_framework import DjangoFilterBackend
from home.filters import ProductFilter
from rest_framework.permissions import IsAuthenticated
from home.pagination import CustomPagination



# Create your views here.
def index(request):
    return render(request, 'index.html')


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('name')
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer
    pagination_class = CustomPagination
    queryset = Tag.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend]

from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Menu, MenuItem
from .serializers import MenuSerializer, MenuItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


MenuItemView = MenuItemsView


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



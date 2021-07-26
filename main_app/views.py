from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import menu

#My awesome home of all things ice cream
def home(request):
    return HttpResponse('<h1>Hello < }}</h1>')

def about(request):
    return render(request, 'about.html')

def menu_index(request):
    return render(request, 'menu/index.html', { 'menu': menu})
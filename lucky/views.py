from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def third(request):
    return HttpResponse('<h1> <marquee> this is first view </marquee></h1>')

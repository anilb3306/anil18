from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def anil(request):
    return HttpResponse('<marquee>welcome to night bar</marquee>')

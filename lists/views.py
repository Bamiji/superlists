from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>') #if type(request) is HttpRequest:
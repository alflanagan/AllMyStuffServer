from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the root URL for a set of web services. It does nothing by itself.")

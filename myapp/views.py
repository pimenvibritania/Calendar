from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("its work")

# Create your views here.

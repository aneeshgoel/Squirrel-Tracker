from django.shortcuts import render

# Create your views here

from django.http import HttpResponse

from .models import Squirrel


def index(request):
    return HttpResponse("Hello, world. You're at the squirrel tracker  index.")




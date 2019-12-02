from django.shortcuts import render


# Create your views here

from django.http import HttpResponse

from .models import Squirrel 


#def index(request):
#    return HttpResponse("Hello, world. You're at the squirrel tracker  index.")

def get_map(request):
    return HttpResponse("Hello this is the map view")


def get_sighting(request):
    return HttpResponse('Hello this is the sigthing view')


def get_particular_sighting(request):
    return HttpResponse('Hello this is a particular sightinig view')


def post_add_sighting(request):
    return HttpResponse('Hello this is a add sighting view')



def delete_sighting(request):
    return HttpResponse('Hello this a view to delete sighting')



def get_stats(request):
    return HttpResponse('Hello this is a view to get stats')


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


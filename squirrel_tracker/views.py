from django.shortcuts import render


# Create your views here

from django.http import HttpResponse

from .models import Squirrel 


#def index(request):
#    return HttpResponse("Hello, world. You're at the squirrel tracker  index.")

def get_map(request):
    sight = Squirrel.objects.all()[:50]
    context ={
            'sightings' :sight,
        }
    return render(request, 'squirrel_tracker/map.html',context)


def get_sighting(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
        }
    return render(request, 'squirrel_tracker/sighting.html',context)


def get_particular_sighting(request, unique_squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_squirrel_ID = unique_squirrel_ID)
    return HttpResponse(squirrel.Unique_squirrel_ID)


def post_add_sighting(request):
    return HttpResponse('Hello this is a add sighting view')



def delete_sighting(request):
    return HttpResponse('Hello this a view to delete sighting')



def get_stats(request):
    return HttpResponse('Hello this is a view to get stats')


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


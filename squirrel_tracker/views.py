from django.shortcuts import render

# Create your views here

from django.http import HttpResponse

from .models import Squirrel


#def index(request):
#    return HttpResponse("Hello, world. You're at the squirrel tracker  index.")

def get_map():



def get_sighting():
    squirrel = Squirrel.objects.all()
    context = {
            'squirrel': squirrel,
        }
    return render(request, 'squirrel_tracker/all.html', context)




def get_particular_sighting():



def post_add_siting():



def delete_sighting():



def get_stats():



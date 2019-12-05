from django.shortcuts import render, redirect


# Create your views here

from django.http import HttpResponse

from .models import Squirrel

from .forms import SquirrelForm


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


def edit_squirrel(request, Unique_squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_squirrel_ID = Unique_squirrel_ID)
    if request.method == "POST":
        form= SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm(instance= squirrel)
    context ={
            'form':form
        }

    return render(request,'squirrel_tracker/edit.html',context)



def add_squirrel(request):
    if request.method == "POST":
        form= SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()
    context ={
            'form':form,
        }
    return render(request,'squirrel_tracker/edit.html',context)




def get_stats(request):
    return HttpResponse('Hello this is a view to get stats')


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


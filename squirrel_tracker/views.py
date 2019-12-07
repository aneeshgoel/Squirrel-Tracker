from django.shortcuts import render, redirect


# Create your views here

from django.http import HttpResponse

from .models import Squirrel

from .forms import SquirrelForm


#def index(request):
#    return HttpResponse("Hello, world. You're at the squirrel tracker  index.")

def main_page(request):
    squirrel = 'Squirrel Tracker'
    return render(request, 'squirrel_tracker/main.html',{'Squirrel': squirrel})

def get_map(request):
    sight = Squirrel.objects.all()[:100]
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
    am_count = 0
    pm_count = 0
    running_count = 0
    foraging_count = 0
    approaches_count = 0
    moans_count = 0
    for  s in  Squirrel.objects.all():
       if s.Shift == 'AM':
           am_count += 1
       elif s.Shift == 'PM':
            pm_count += 1
       if s.Running == True:
            running_count += 1
       if s.Foraging == True:
            foraging_count += 1
       if s.Approaches == True:
            approaches_count += 1
       if s.Moans == True:
            moans_count += 1
    context ={ 
             'AM_count' : am_count,
             'PM_count' : pm_count,
             'Running_count' : running_count,
             'Foraging_count' : foraging_count,
             'Approaches_count' : approaches_count,
             'Moans_count' : moans_count,
        }
    return render(request, 'squirrel_tracker/stat.html', context)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


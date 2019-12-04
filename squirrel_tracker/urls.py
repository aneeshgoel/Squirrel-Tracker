from django.urls import path

from . import views

urlpatterns = [
    path('map', views.get_map, name='map'),
    path('sightings/',views.get_sighting, name='sighting'),
    path('sightings/<str:unique_squirrel_ID>/',views.get_particular_sighting, name = 'particular_sighting'),
    path('sightings/add',views.post_add_sighting, name = 'add_sighting'),
    path('sightings/12', views.delete_sighting, name = 'delete_sighting'),
    path('sightings/stats', views.get_stats, name = 'stats'),
    ]

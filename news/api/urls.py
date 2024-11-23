from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('news/', views.data_list),
    path('politics/', views.politics_list),
    path('economy/', views.economy_list),
    path('sports/', views.sports_list),
    path('science/', views.science_list),
    path('world/', views.world_list),
    path('space/', views.space_list),
    path('society/', views.society_list),
    path('environemnt/', views.environment_list),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('news/', views.data_list),
    path('politics/', views.politics_list),
    path('economy/', views.economy_list),
    path('sports/', views.sports_list),
    path('test/', views.test),
]
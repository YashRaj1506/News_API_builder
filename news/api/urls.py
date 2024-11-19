from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('news/', views.data_list),
    path('politics/', views.politics_list),
]
from django.shortcuts import render
from news.api.models import News_data

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

def homepage(request):
    return render(request, 'index.html')


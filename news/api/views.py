from django.shortcuts import render
from news.api.models import News_data
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from news.api.models import News_data
from news.api.serializers import Data_Serializer

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

def homepage(request):
    return render(request, 'index.html')


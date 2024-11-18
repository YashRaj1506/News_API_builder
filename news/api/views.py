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

@csrf_exempt
def data_list(request):
    """
    Lists all data on the Web UI
    """

    if request.method == 'GET':
        snippets = News_data.objects.all()
        serializer = Data_Serializer(News_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Data_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
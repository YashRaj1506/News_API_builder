from django.shortcuts import render
from .models import News_data
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from news.api.models import News_data
from .serializers import Data_Serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

def homepage(request):
    return render(request, 'index.html')

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def data_list(request):
    """
    Lists all data on the Web UI
    """

    if request.method == 'GET':
        data = News_data.objects.all()
        serializer = Data_Serializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Data_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return Response(serializer.errors, status=400)
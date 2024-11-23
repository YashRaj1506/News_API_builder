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
from .tasks import test_func


from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


def homepage(request):
    return render(request, "index.html")


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def data_list(request):
    """
    Lists all data on the Web UI
    """
    if request.method == "GET":
        data = News_data.objects.all()
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = Data_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def politics_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="politics")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def sports_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="sports")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def economy_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="economy")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def world_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="world")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def science_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="science")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def space_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="space")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def society_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="society&arts")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
@permission_classes([AllowAny])
def environment_list(request):

    if request.method == "GET":
        data = News_data.objects.filter(category="environment")
        serializer = Data_Serializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

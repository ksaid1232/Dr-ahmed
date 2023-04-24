from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import ProductModel
# Create your views here.


@api_view(["GET"])
def Products_list(request):
    data = ProductModel.objects.all()
    serializer = ProductSerializer(data, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def Product_Details(request, id):
    print(id)
    data = ProductModel.objects.get(pk=id)
    serializer = ProductSerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
def Featured_list(request):
    data = ProductModel.objects.all().order_by('-id')
    serializer = ProductSerializer(data[0:5], many=True)
    return Response(serializer.data)

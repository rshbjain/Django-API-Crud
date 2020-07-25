from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Database
from .serializers import DatabaseSerializer
from rest_framework.decorators import api_view

#decorater
@api_view(['GET'])   #READ
#defined function with requests as argument
def databaselist(request):
    #query over the database model in models.py
    databases = Database.objects.all()
    #variable that takes the query as the input
    serializer = DatabaseSerializer(databases,many = True)
    #returning query in json format
    return Response(serializer.data)
    

#decorater
@api_view(['POST'])    #CREATE
#defined function with requests as argument
def postdetails(request):
    #taking the data in the json format
    serializer = DatabaseSerializer(data = request.data)

    #if the json data is valid
    if serializer.is_valid():
        #query as the output
        serializer.save()
    #gives the response when runs successfully
    return Response(serializer.data)


#decorator
@api_view(['POST'])     #UPDATE
#defined function with requests and primary key as argument
def databaseUpdate(request , pk):
    #query over the feilds in model with argument as"pk"
    databases = Database.objects.get (id = pk)
    #object serializer requesting data in the json format
    serializer = DatabaseSerializer(instance=databases,data = request.data)

    #if valid
    if serializer.is_valid():
        #return data as query
        serializer.save()
    #gives the response when done right
    return Response(serializer.data)


#decorator
@api_view(['DELETE'])       #DELETE
#defined function with requests and primary key as argument
def databaseDelete(request , pk):
    #query on database with a particular id
    databases = Database.objects.get (id = pk)
    #delete the data of that id
    databases.delete()
    #gives the response when done
    return Response('{message : DELETED}')



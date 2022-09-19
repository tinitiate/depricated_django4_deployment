from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from random import randint


#####################################################################################
@api_view(['GET', 'POST', 'PUT','PATCH'])
def random_number(request):
    
    if request.method == "GET":
        return Response({"GETdata": randint(10, 20)}, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        return Response({"POSTdata": randint(21, 30)}, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        return Response({"PUTdata": randint(31, 100)}, status=status.HTTP_200_OK)
    
    else:
        data = {"Error SEP2022 Batch": {"status": 400,"message": "Request Error"}}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


#####################################################################################
def evenodd(n1):
    if n1%2 == 0:
        return {n1:'is EVEN'}
    else:
        return {n1:'is ODD'}

@api_view(['GET', 'POST'])
def even_odd(request):
    
    if request.method == 'GET': # and 'N1' in request.GET:
        #
        #######################
        # Read Body Variables
        #######################
        # request.GET is the body parameter dictionary
        data = request.GET['N1']
        print("this is the data",data)
        
        return Response(evenodd(int(data)), status=status.HTTP_200_OK)
    #    
    elif request.method == 'POST': # and 'N1' in request.POST:
    
        #######################
        # Read Body Variables
        #######################
        # request.POST is the parameter dictionary        
        data = request.POST['N1']
        print("this is the data",data)
        return Response(evenodd(int(data)), status=status.HTTP_200_OK)
    #
    else:
        data = {"Error": {"status": 400,
                          "message": "Expected N1 Integer Parameter"}}

        return Response(data, status=status.HTTP_400_BAD_REQUEST)


#####################################################################################
@api_view(['GET', 'POST'])
def get_custom_header(request):

    if request.method == "GET":
        #
        #######################
        # Read Header Variables
        #######################
        l_header_prefix = 'HTTP_'
        # Header Parameter Dictionary
        H1 = request.META[l_header_prefix+'H1']

        l_return = {"GET Custom Header Data H1":H1}
        return Response(l_return, status=status.HTTP_200_OK)
    #
    elif request.method == "POST":
        #
        #######################
        # Read Header Variables
        #######################
        l_header_prefix = 'HTTP_'
        # Header Parameter Dictionary
        H1 = request.META[l_header_prefix+'H1']

        l_return = {"POST Custom Header Data H1":H1}
        return Response(l_return, status=status.HTTP_200_OK)
    #
    else:
        data = {"Error": {"status": 400,
                          "message": "Request Error"}}

        return Response(data, status=status.HTTP_400_BAD_REQUEST)

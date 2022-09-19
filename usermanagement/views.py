from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view

class data_set(View):

    authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponse("You are Authenticated to see this, welcome.")
        else:
            return HttpResponse("You are Authenticated to see this, welcome.")

    def post(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            return HttpResponse("You are Authenticated to see this, welcome.")
        else:
            return HttpResponse("You are Authenticated to see this, welcome.")
        # print(self.permission_classes)
        # return HttpResponse("Welcome to SyntaxBoard Django Test Home Page Version 1.0")



@api_view(['GET', 'POST'])
def secure_page(request):
    authentication_classes=[JWTAuthentication]
    if request.user.is_authenticated:
        return HttpResponse("This is a secure page")
    else:
        return HttpResponse("You are not authorized to see this page")
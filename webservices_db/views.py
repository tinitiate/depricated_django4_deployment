from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view

from .model_customer import Customer
from .customerserializer import CustomersSerializer
# import json


# Create your views here.
class GetCustomer(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer

class GetAllCustomers(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer

class InsertCustomerData(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer

class UpdateCustomerData(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer

class DeleteCustomerData(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomersSerializer

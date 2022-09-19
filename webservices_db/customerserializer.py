from rest_framework import serializers 
from .model_customer import Customer 

class CustomersSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Customer
        fields = ['customer_id', 'customer_name', 'application_date', 'customer_creditscore', 'customer_req_loanamount']
        # fields = "__all__"


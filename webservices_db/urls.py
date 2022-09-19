from django.urls import path
from . import views


urlpatterns = [
    # path("updateMany",views.updateMany),
    path("get_customer_details",views.GetAllCustomers.as_view()),
    path("insert_customer_details", views.InsertCustomerData.as_view()),
    path("update_customer_details/<int:pk>",views.UpdateCustomerData.as_view()),
    path("delete_customer_details/<int:pk>",views.DeleteCustomerData.as_view()),
]


## ##################################################################################
## TESTING
## ##################################################################################

# http://127.0.0.1:8000/webservices_db/get_customer_details
"""
Use the method = GET HTTP  in postman
"""

# http://127.0.0.1:8000/webservices_db/insert_customer_details
"""
# With postman apply the following
1. Method = POST 
2. Content = Body>Raw
3. type = JSON

content
--------
{
    "customer_id": 4
    ,"customer_name":"D"
    ,"application_date":"2022-01-02"
    ,"customer_creditscore":333
    ,"customer_req_loanamount":1234.45
}
"""

# http://127.0.0.1:8000/webservices_db/update_customer_details/4
"""
# With postman apply the following
1. Method = PUT 
2. Content = Body>Raw
3. type = JSON

content
--------
{
     "customer_id": 4
    ,"customer_name":"HHHHHHH"
    ,"application_date":"2021-08-20"
}

"""


# http://127.0.0.1:8000/webservices_db/delete_customer_details/4
"""
# With postman apply the following
1. Method = DELETE 
No Content To Pass
"""

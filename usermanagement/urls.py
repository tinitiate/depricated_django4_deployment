
from django.conf.urls import include
from django.urls import path
# from django.urls import re_path as url
from .views import data_set
from . import views

urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('dataset/',data_set.as_view()),
    path('func_test/',views.secure_page),
]


# ########################################################
# Create User and Get Token in Browser
# ########################################################
# http://127.0.0.1:8000/usermanagement/users
# Create a username
# set password
# Example:
# tester
# Password!23

# Get user information
# http://127.0.0.1:8000/usermanagement/users/me/

# Get token
# http://127.0.0.1:8000/usermanagement/token/login/

# Logout
# http://127.0.0.1:8000/usermanagement/token/logout/

# ########################################################


# ########################################################
# Testing Token Authentication in Postman
# ########################################################

# Step 1:
# in URL use http://127.0.0.1:8000/usermanagement/token/login/
# HTTP Type: POST
# body > form-data >
# username: tester
# password: Password!23
# Submit and copy the Auth Token

# Step 2:
# in the URL use http://127.0.0.1:8000/usermanagement/dataset/
# HTTP Type: GET
# Headers > X-CSRFToken > paste the Auth Token from Step 1.

# ########################################################
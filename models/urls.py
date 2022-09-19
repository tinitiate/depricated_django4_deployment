# from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
#########################################################
# CUSTOM SQL
#########################################################
path('sql_createcustomersdata/',views.sql_createcustomersdata),
path('sql_getcustomerbyid/<int:in_customer_id>',views.sql_getcustomerbyid),
path('sql_updatecustomernamebyid/<int:in_customer_id>/<str:in_customer_name>',views.sql_updatecustomernamebyid),
path('sql_deleterecordbyid/<int:in_customer_id>',views.sql_deleterecordbyid),

#########################################################
# ORM Object Relational Mapping
#########################################################
path('orm_createcustomersdata/',views.orm_createcustomersdata),
path('orm_updatecustomernamebyid/<int:in_customer_id>/<str:in_customer_name>',views.orm_updatecustomernamebyid),
path('orm_deleterecordbyid/<int:in_customer_id>',views.orm_deleterecordbyid),
path('orm_deleteallrecords/',views.orm_deleteallrecords),
path('orm_getallrecords/',views.orm_getallrecords),
path('orm_getrecordbyid/<int:in_customer_id>',views.orm_getrecordbyid),
]

#########################################################
# TESTING: ORM Object Relational Mapping
#########################################################
# http://localhost:8000/models/orm_createcustomersdata/
# http://localhost:8000/models/orm_updatecustomernamebyid/1/eee
# http://localhost:8000/models/orm_deleterecordbyid/1
# http://localhost:8000/models/orm_deleteallrecords/
# http://localhost:8000/models/orm_getallrecords/
# http://localhost:8000/models/orm_getrecordbyid/1

#########################################################
# TESTING: CUSTOM SQL
#########################################################
# http://localhost:8000/models/sql_createcustomersdata/
# http://localhost:8000/models/sql_getcustomerbyid/11
# http://localhost:8000/models/sql_updatecustomernamebyid/11/eee
# http://localhost:8000/models/sql_deleterecordbyid/11


# Django Tutorial 3
> Venkata Bhattaram (c)



## Django Models, Webservices and Authentication

* Models
  * Working with DB Tables
* Webservices 
  * Functions
  * Database CRUD
* Users Management
* Authentication


### Prerequisites

* Create DB in postgresql DB with the script `postgresql_loan_management_db.sql`
* `pip install Django psycopg2`
* `pip install djangorestframework`
* `pip install djoser`


### Project

* **STEP 1** Create the project
```bash
django-admin startproject syntaxboard_django_3
```

* **STEP 2** Create Apps
```
python manage.py startapp models
python manage.py startapp webservices
python manage.py startapp webservices_db
python manage.py startapp usermanagement
```

* **STEP 3** Create `dbrouters.py`

* **STEP 4** Edit `settings.py`
* For User Management
```
Add the following 3rd party APPS to teh settings.py
#############################
# Rest 3rd party, Add these
'rest_framework',
# User management 3rd party, Add these
'rest_framework.authtoken',
'djoser',
#############################
```


* Add the DJOSER Settings
```
#################################################
# DJOSER Settings Start
#################################################
#configure DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# DJOSER CONFIG
DJOSER = {
    "USER_ID_FIELD": "username"
}

#################################################
# DJOSER Settings End
#################################################
```


* **STEP 5** Edit projects `urls.py`

* **STEP 6** Inspect DB to generate model, using the `inspectdb` command
```
python manage.py inspectdb --database LOANS customer > models/customer.py
python manage.py inspectdb --database LOANS customer > webservices_db/customer.py
```

* **STEP 7** Make Migrations and Migrate
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

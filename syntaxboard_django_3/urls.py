# djangomodels/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('models/', include('models.urls')),
    path('webservices/', include('webservices.urls')),
    path('webservices_db/', include('webservices_db.urls')),
    path('usermanagement/', include('usermanagement.urls')),
    #path('authentication/', include('authentication.urls')),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('bio.urls')),
]

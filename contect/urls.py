from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('contect/', views.contect, name='contect'),
]

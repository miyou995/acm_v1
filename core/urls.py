from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required, permission_required
from .views import IndexView
app_name= 'core'

urlpatterns = [
  
  path('', login_required(IndexView.as_view()), name='index'),
   ]


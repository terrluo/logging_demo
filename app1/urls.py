#!/usr/bin/python
from django.urls import path

from app1 import views

app_name = 'app1'

urlpatterns = [
    path('', views.App1ListView.as_view(), name='list'),
]

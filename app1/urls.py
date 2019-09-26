#!/usr/bin/python
from django.urls import path

from app1 import views

urlpatterns = [
    path('', views.App1ListView.as_view(), name='app1-list'),
]

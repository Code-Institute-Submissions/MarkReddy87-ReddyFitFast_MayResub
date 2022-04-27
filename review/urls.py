""" Add relevant imports below """
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review'),
    path('add/', views.add_review, name='add_review'),
]

""" Add relevant imports below """
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review'),
    path('add/', views.add_review, name='add_review'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
]

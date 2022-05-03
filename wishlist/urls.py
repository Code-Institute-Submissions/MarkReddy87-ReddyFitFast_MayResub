""" Add relevant imports below """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
]

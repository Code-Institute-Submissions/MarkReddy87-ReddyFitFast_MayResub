""" Add relevant imports below """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist/add_to_wishlist/<int:product_id>/',
         views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove_from_wishlist/<int:product_id>/',
         views.remove_from_wishlist, name='remove_from_wishlist'),
]

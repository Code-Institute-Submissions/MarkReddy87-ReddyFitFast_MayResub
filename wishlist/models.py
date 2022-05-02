""" Relevant imports below """
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishList(models.Model):
    """ Wishlist items model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wished_items = models.ManyToManyField(Product)

    def __str__(self):
        return self.user

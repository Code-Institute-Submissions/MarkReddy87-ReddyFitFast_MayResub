""" relevant imports below """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishList
from products.models import Product


# @login_required
# def show_wishlist(request):
#     """ view to show wishlist """
#     wish_items = WishList.objects.all()
#     template = 'whishlist/wishlist.html'
#     context = {
#         'wished_items': wish_items,
#     }

#     return render(request, template, context)

@login_required
def show_wishlist(request):
    """ view to show wishlist """
    wish_items = None
    try:
        wish_items = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    context = {
        'wish_items': wish_items,
    }

    return render(request, 'whishlist/wishlist.html', context)

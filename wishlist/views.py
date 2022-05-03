""" relevant imports below """
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import WishList


@login_required
def wishlist(request):
    """ view to show wishlist """
    products = None
    products = WishList.objects.filter(user=request.user)
    context = {
        'products': products,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    A view to create wishlist if the user does not have one.
    This will also add and remove the product from the wishlist.
    """
    product = get_object_or_404(Product, id=product_id)
    user_wishlist, _ = WishList.objects.get_or_create(user=request.user)
    if user_wishlist.wished_items.filter(id=request.user.id).exists():
        user_wishlist.wished_items.remove(product)
        messages.success(request,
                         'Product successfully removed from wishlist!')
    else:
        user_wishlist.wished_items.add(product)
        messages.success(request, 'Successfully added product to wishlist!')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

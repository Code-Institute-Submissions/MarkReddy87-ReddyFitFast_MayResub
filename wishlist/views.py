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
    wishlist = None
    wishlist = WishList.objects.filter(user=request.user)
    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ Add to wishlist view """
    product = get_object_or_404(Product, id=product_id)
    wishlist, _ = WishList.objects.get_or_create(user=request.user)
    if wishlist.wished_items.filter(id=request.user.id).exists():
        wishlist.wished_items.remove(product)
        messages.success(request,
                         'Product successfully removed from wishlist!')
    else:
        wishlist.wished_items.add(product)
        messages.success(request, 'Successfully added product to wishlist!')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

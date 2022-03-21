from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ Checkout view """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There are no items in your shopping bag right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KU8IUDYfHuMwm0kS2ub6kUuMbvtuyWhnHgJ3LPfBQsDJnWNsFRKA30sXZbHZBhkmk00wQnKVZRx0JFkO8zW1lS400nxo4SbmO',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

""" imports below """
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInLine(admin.TabularInline):
    """ Allows us to add and edit line items """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Adding order fields to admin page """
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ('order_number', 'date', 'order_total',
                       'original_bag', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

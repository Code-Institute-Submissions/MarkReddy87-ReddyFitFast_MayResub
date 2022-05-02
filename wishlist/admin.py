from django.contrib import admin
from .models import WishList


class WishListAdmin(admin.ModelAdmin):
    """ Wishlist admin """

    list_display = ('user',)


admin.site.register(WishList, WishListAdmin)

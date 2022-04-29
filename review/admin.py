from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """ Review Admin setup """

    list_display = ('title', 'created_on',)
    search_fields = ['title', 'body']
    list_filter = ('created_on',)


admin.site.register(Review, ReviewAdmin)

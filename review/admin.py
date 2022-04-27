from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """ Review Admin setup """

    prepopulated_fields = {'slug': ('title',)}

    list_display = ('title', 'slug', 'created_on',)
    search_fields = ['title', 'body']
    list_filter = ('created_on',)


admin.site.register(Review, ReviewAdmin)

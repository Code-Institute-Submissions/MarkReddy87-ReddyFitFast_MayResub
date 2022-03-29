from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """ Review Admin setup """
    fields = ('title', 'body', 'image', 'posted_by',
              'created_on', 'approved',)

    list_filter = ('approved', 'created_on')

    ordering = ('-created_on')

    def approved_review(self, request, queryset):
        """ approved function """
        queryset.update(approved=True)


admin.site.register(Review)

from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'owner_name', 'name')
    list_display_links = ('id', 'title')
    list_filter = ('name',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price', 'list_date', 'owner_name', 'name', 'address ',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)

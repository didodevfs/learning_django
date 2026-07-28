from django.contrib import admin
from gallery.models import Photograph

class ListingPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_per_page = 10

admin.site.register(Photograph, ListingPhotographs)
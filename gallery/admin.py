from django.contrib import admin
from gallery.models import Photograph

class ListingPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "subtitle")
    list_display_links = ("id", "name")
    search_fields = ("name",)

admin.site.register(Photograph, ListingPhotographs)
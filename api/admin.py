from django.contrib import admin

# Register your models here.
from .models import Items, Location

admin.site.register(Items)
admin.site.register(Location)
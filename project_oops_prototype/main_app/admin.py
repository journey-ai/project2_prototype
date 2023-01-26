from django.contrib import admin
from .models import Station_search

# Register your models here.


class Station_search_Admin(admin.ModelAdmin):
    search_fields = ['words']

admin.site.register(Station_search, Station_search_Admin)
from django.contrib import admin
from .models import Servicio, Plan

# Register your models here.

class PlanesAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','servicio']
    search_fields = ['nombre','precio']
    list_filter = ['servicio']
    list_per_page = 10

admin.site.register(Servicio)
admin.site.register(Plan, PlanesAdmin)
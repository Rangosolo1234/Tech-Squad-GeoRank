from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Incidences
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')

admin.site.register(Incidences, IncidencesAdmin)

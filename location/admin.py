from django.contrib import admin
from location.models import Location
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
        list_display = ('title','description')

admin.site.register(Location,LocationAdmin)    

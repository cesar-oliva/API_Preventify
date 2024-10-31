from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_advertising import AdvertisingResource
from preventify.models.models_advertising import Advertising

# Register your models here.

class AdvertisingAdmin(ImportExportModelAdmin):
    resource_classes = [AdvertisingResource]
    list_display = ('id',) 

admin.site.register(Advertising, AdvertisingAdmin)




from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_advertising_player import AdvertisingPlayerResource
from preventify.models.models_advertising_player import AdvertisingPlayer

# Register your models here.

class AdvertisingPlayerAdmin(ImportExportModelAdmin):
    resource_classes = [AdvertisingPlayerResource]
    list_display = ('id',) 

admin.site.register(AdvertisingPlayer, AdvertisingPlayerAdmin)




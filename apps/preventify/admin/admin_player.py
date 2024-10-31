from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_player import PlayerResource
from preventify.models.models_player import Player


# Register your models here.

class PlayerAdmin(ImportExportModelAdmin):
    resource_classes = [PlayerResource]
    list_display = ('username',) 

admin.site.register(Player, PlayerAdmin)




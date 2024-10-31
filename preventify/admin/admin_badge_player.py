from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_badge_player import BadgePlayerResource
from preventify.models.models_badge_player import BadgePlayer

# Register your models here.

class BadgePlayerAdmin(ImportExportModelAdmin):
    resource_classes = [BadgePlayerResource]
    list_display = ('date_obtained',) 

admin.site.register(BadgePlayer, BadgePlayerAdmin)




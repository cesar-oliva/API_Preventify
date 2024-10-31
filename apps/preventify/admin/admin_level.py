from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_level import LevelResource
from preventify.models.models_level import Level


# Register your models here.

class LevelAdmin(ImportExportModelAdmin):
    resource_classes = [LevelResource]
    list_display = ('description',) 

admin.site.register(Level, LevelAdmin)


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_badge import BadgeResource
from preventify.models.models_badge import Badge

# Register your models here.

class BadgeAdmin(ImportExportModelAdmin):
    resource_classes = [BadgeResource]
    list_display = ('description',) 

admin.site.register(Badge, BadgeAdmin)




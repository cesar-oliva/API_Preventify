from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_advice import AdviceResource
from preventify.models.models_advice import Advice
# Register your models here.

class AdviceAdmin(ImportExportModelAdmin):
    resource_classes = [AdviceResource]
    list_display = ('description',) 

admin.site.register(Advice, AdviceAdmin)




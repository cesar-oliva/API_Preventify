from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_token import TokenResource
from preventify.models.models_token import Token


# Register your models here.

class TokenAdmin(ImportExportModelAdmin):
    resource_classes = [TokenResource]
    list_display = ('description',) 

admin.site.register(Token, TokenAdmin)


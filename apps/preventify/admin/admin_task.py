from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_task import TaskResource
from preventify.models.models_task import Task

# Register your models here.

class TaskAdmin(ImportExportModelAdmin):
    resource_classes = [TaskResource]
    list_display = ('description',) 

admin.site.register(Task, TaskAdmin)




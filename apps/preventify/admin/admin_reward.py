from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from preventify.Resources.resources_reward import RewardResource
from preventify.models.models_reward import Reward


# Register your models here.

class RewardAdmin(ImportExportModelAdmin):
    resource_classes = [RewardResource]
    list_display = ('date_obtained',) 

admin.site.register(Reward, RewardAdmin)



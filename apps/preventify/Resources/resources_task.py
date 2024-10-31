from import_export import resources
from preventify.models.models_task import Task

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class TaskResource(resources.ModelResource):
    class Meta:
        model = Task


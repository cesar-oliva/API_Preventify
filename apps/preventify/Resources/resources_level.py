from import_export import resources
from preventify.models.models_level import Level

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class LevelResource(resources.ModelResource):
    class Meta:
        model = Level


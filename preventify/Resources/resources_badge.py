from import_export import resources
from preventify.models.models_badge import Badge

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class BadgeResource(resources.ModelResource):
    class Meta:
        model = Badge


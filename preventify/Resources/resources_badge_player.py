from import_export import resources
from preventify.models.models_badge_player import BadgePlayer

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class BadgePlayerResource(resources.ModelResource):
    class Meta:
        model = BadgePlayer


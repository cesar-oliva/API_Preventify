from import_export import resources
from preventify.models.models_player import Player

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class PlayerResource(resources.ModelResource):
    class Meta:
        model = Player 


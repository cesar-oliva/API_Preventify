from import_export import resources
from preventify.models.models_advertising_player import AdvertisingPlayer

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class AdvertisingPlayerResource(resources.ModelResource):
    class Meta:
        model = AdvertisingPlayer


from import_export import resources
from preventify.models.models_advertising import Advertising

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class AdvertisingResource(resources.ModelResource):
    class Meta:
        model = Advertising


from import_export import resources
from preventify.models.models_token import Token

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class TokenResource(resources.ModelResource):
    class Meta:
        model = Token 


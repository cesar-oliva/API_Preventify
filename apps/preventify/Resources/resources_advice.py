from import_export import resources
from preventify.models.models_advice import Advice

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class AdviceResource(resources.ModelResource):
    class Meta:
        model = Advice


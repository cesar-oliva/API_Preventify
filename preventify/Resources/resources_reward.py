from import_export import resources
from preventify.models.models_reward import Reward

#Resource defines how objects are mapped to their import 
# and export representations and handle importing and exporting data.

class RewardResource(resources.ModelResource):
    class Meta:
        model = Reward 


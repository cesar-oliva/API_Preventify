# Create your models here.
from django.db import models
from preventify.models.models_reward import Reward


# Create your models here.
class Advertising(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'advertising'
        verbose_name_plural = 'advertisings'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)


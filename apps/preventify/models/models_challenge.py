# Create your models here.
from django.db import models
from preventify.models.models_reward import Reward
from preventify.models.models_event import Event


# Create your models here.
class Challenge(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'challenge'
        verbose_name_plural = 'challenges'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)


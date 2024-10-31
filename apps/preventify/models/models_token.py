# Create your models here.
from django.db import models
from preventify.models.models_reward import Reward


# Create your models here.
class Token(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'token'
        verbose_name_plural = 'tokens'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    is_consumable = models.BooleanField(default=False)
    reward = models.ManyToManyField(Reward, through='TokenReward', blank=True)


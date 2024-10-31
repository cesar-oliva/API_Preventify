# Create your models here.
from django.db import models


# Create your models here.
class Reward(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'reward'
        verbose_name_plural = 'rewards'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    date_obtained = models.DateTimeField()



# Create your models here.
from django.db import models


# Create your models here.
class Level(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'level'
        verbose_name_plural = 'levels'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    expirience_needed = models.CharField(editable=True, max_length=10, verbose_name='experience_needed')


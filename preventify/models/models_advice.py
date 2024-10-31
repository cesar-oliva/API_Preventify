# Create your models here.
from django.db import models


# Create your models here.
class Advice(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'advice'
        verbose_name_plural = 'advices'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    status = models.BooleanField(default=True)
 
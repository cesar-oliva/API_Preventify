# Create your models here.
from django.db import models


# Create your models here.
class Event(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

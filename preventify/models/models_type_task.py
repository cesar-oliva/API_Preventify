# Create your models here.
from django.db import models


# Create your models here.
class TypeTask(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'type_task'
        verbose_name_plural = 'type_tasks'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')



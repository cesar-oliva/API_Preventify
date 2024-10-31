# Create your models here.
from django.db import models
from preventify.models.models_challenge import Challenge
from preventify.models.models_type_task import TypeTask

# Create your models here.
class Task(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    type_task = models.ForeignKey(TypeTask, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)


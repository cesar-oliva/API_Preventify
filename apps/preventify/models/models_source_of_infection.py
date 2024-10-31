# Create your models here.
from django.db import models
from preventify.models.models_task_player import TaskPlayer

# Create your models here.
class SourceOfInfection(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'source_of_infection'
        verbose_name_plural = 'source_of_infections'

    class Type_Risk(models.TextChoices):
        HIGH = 'H',
        LOW = 'L',
        MEDIUM = 'M'

    def __str__(self):
        cadena = (self.id)
        return cadena
    
    description = models.CharField(editable=True, max_length=100, verbose_name='description')
    image = models.ImageField()
    coordinates = models.CharField(editable=True, max_length=100, verbose_name='coordinates')
    risk = models.CharField(max_length=1,choices= Type_Risk.choices)
    task_player = models.ManyToManyField(TaskPlayer, through='SourceOfInfectionTaskPlayer', blank=True)

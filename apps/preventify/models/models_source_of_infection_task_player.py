from django.db import models
from preventify.models.models_source_of_infection import SourceOfInfection
from preventify.models.models_task_player import TaskPlayer

# Create your models here.
class SourceOfInfectionTaskPlayer(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'source_of_infection_task_player'
        verbose_name_plural = 'source_of_infection_task_players'
        ordering = ['id',]

    def __str__(self):
        cadena = str(self.id)
        return cadena
    
    source_of_infection = models.ForeignKey(SourceOfInfection, on_delete=models.CASCADE)
    taskplayer = models.ForeignKey(TaskPlayer, on_delete=models.CASCADE)

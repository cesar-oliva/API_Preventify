from django.db import models
from preventify.models.models_player import Player
from preventify.models.models_task import Task



# Create your models here.
class TaskPlayer(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'task_player'
        verbose_name_plural = 'task_players'
        ordering = ['id',]

    def __str__(self):
        cadena = str(self.id)
        return cadena
    
    status = models.BooleanField(default=True, verbose_name='status')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

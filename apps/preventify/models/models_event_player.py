from django.db import models
from preventify.models.models_player import Player
from preventify.models.models_event import Event


# Create your models here.
class EventPlayer(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'event_player'
        verbose_name_plural = 'event_players'
        ordering = ['id',]

    def __str__(self):
        cadena = str(self.id)
        return cadena
    
    status = models.BooleanField(default=True, verbose_name='status')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

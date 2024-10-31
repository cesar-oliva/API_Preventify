from django.db import models
from preventify.models.models_player import Player
from preventify.models.models_advertising import Advertising


# Create your models here.
class AdvertisingPlayer(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'advertising_player'
        verbose_name_plural = 'advertising_players'
        ordering = ['id',]

    def __str__(self):
        cadena = str(self.id)
        return cadena
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    advertising = models.ForeignKey(Advertising, on_delete=models.CASCADE)


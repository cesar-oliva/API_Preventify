from django.db import models
from preventify.models.models_player import Player
from preventify.models.models_badge import Badge


 # Create your models here.
class BadgePlayer(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'badge_player'
        verbose_name_plural = 'badge_players'
        ordering = ['id',]

    def __str__(self):
        cadena = str(self.id)
        return cadena
    
    date_obtained = models.DateTimeField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

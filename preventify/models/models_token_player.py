from django.db import models
from preventify.models.models_player import Player
from preventify.models.models_token import Token


# Create your models here.
class TokenPlayer(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'token_player'
        verbose_name_plural = 'token_players'
        ordering = ['id',]

    def __str__(self):
        cadena = str(self.id)
        return cadena
    
    quantity = models.IntegerField(verbose_name='quantity')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tokens = models.ForeignKey(Token, on_delete=models.CASCADE)

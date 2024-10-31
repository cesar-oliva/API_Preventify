from django.db import models
from preventify.models.models_reward import Reward
from preventify.models.models_token import Token

# Create your models here.
class TokenReward(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'token_reward'
        verbose_name_plural = 'token_rewards'
        ordering = ['id',]

    def __str__(self):
        cadena = str(self.id)
        return cadena
    
    quantity = models.IntegerField(verbose_name='quantity')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    tokens = models.ForeignKey(Token, on_delete=models.CASCADE)

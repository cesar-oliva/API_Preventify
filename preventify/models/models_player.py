
# Create your models here.
from django.db import models
from preventify.models.models_level import Level
from preventify.models.models_advertising import Advertising
from preventify.models.models_token import Token
from preventify.models.models_task import Task
from preventify.models.models_event import Event
from preventify.models.models_badge import Badge

# Create your models here.
class Player(models.Model):
    class Meta:
        app_label = 'preventify'
        verbose_name = 'player'
        verbose_name_plural = 'players'

    def __str__(self):
        cadena = (self.username)
        return cadena
    
    username = models.CharField(editable=True, max_length=30, verbose_name='username')
    expirience = models.CharField(editable=True, max_length=10, verbose_name='experience')
    nivel = models.ForeignKey(Level, on_delete=models.CASCADE)
    advertising = models.ManyToManyField(Advertising, through='AdvertisingPlayer', blank=True)
    task = models.ManyToManyField(Task, through='TaskPlayer', blank=True)
    token = models.ManyToManyField(Token, through='TokenPlayer', blank=True)
    event = models.ManyToManyField(Event, through='EventPlayer', blank=True)
    badge = models.ManyToManyField(Badge, through='BadgePlayer', blank=True)


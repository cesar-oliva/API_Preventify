from django.urls import path, include
from rest_framework import routers
from preventify.view.views_player import PlayerViewSet
from preventify.view.views_token import TokenViewSet
from preventify.view.views_badge import BadgeViewSet
from preventify.view.views_reward import RewardViewSet
from preventify.view.views_task import TaskViewSet
from preventify.view.views_level import LevelViewSet
from preventify.view.views_event import EventViewSet
from preventify.view.views_token_player import TokenPlayerViewSet

router = routers.DefaultRouter()
router.register(r'Player',PlayerViewSet)
router.register(r'Token',TokenViewSet)
router.register(r'Badge',BadgeViewSet)
router.register(r'Reward',RewardViewSet)
router.register(r'Task',TaskViewSet)
router.register(r'Level',LevelViewSet)
router.register(r'Event',EventViewSet)
router.register(r'TokenPlayer',TokenPlayerViewSet)

urlpatterns =[
    path('',include(router.urls)),
]
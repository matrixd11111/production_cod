from django.urls import path
from .views import *

app_name = 'minigames'

urlpatterns = [
    path('index', index, name='index'),
    path('lotogame/', lotogame, name='lotogame'),
    path('newticket/<int:menu>/', GameMenuViews.as_view(url='/minigame/lotogame/'), name='menu'),
    path('chengeticket/<int:pk>/<int:ticket>/', ChengeTicketViews.as_view(url='/minigame/lotogame/'), name='chenge_ticket'),
    path('test/', test, name='test')

]

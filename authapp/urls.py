from django.urls import path
from django.conf.urls import include
from .views import *

app_name = 'authapp'

urlpatterns = [
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registred/', registred, name='registred'),
]

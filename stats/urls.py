from django.urls import path, include
from .views import *

# Define your urls here.
app_name = 'stats'

urlpatterns = [
    path('estadisticas', Estadisticas.as_view(), name='estadisticas')
]
from django.urls import path, include
from .views import *

# Define your urls here.
app_name = 'partidas'

urlpatterns = [
    path('', Partidas.as_view(), name='partidas'),
    path('crear_partida', CrearPartida.as_view(), name='crear_partida'),
    path('entrar_partida', UnirseAPartida.as_view(), name='entrar_partida'),
    path('jugar/<int:pk>/', Jugar.as_view(), name='jugar'),
    path('resultado', Resultado.as_view(), name='resultado'),
    path('resultado2', ResultadoPartida.as_view(), name='resultado2'),
    path('rooms', Rooms.as_view(), name='rooms'),
    
]

from django.urls import path, include
from .views import *

# Define your urls here.
app_name = 'partidas'

urlpatterns = [
    path('partidas', Partidas.as_view(), name='partidas'),
    
]

from django.urls import path
from .views import *

# Define your urls here.
app_name = 'menu'

urlpatterns = [
    path('menu', Menu.as_view(), name='menu'),
    
]

import random
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from .models import Partida, Tablero

# Create your views here.



class CrearPartida(View):

    template_name = 'partidas/rooms.html'

    def get(self, request):
        codigo_partida = random.choice(range(10000000, 100000000))
        usuario_creador = request.user
        partida = Partida.objects.create(codigo_partida=codigo_partida, partida_privada=True, jugador_x=usuario_creador)
        Tablero.objects.create(partido=partida)
        context = {'partida': partida, 'user': request.user}
        return render(request, self.template_name, context=context)

class UnirseAPartida(View):

    template_name = 'partidas/rooms.html'

    def post(self, request):
        codigo_partida = request.POST.get('codigo_partida')
        partida = Partida.objects.get(codigo_partida=codigo_partida)
        context = {'partida': partida, 'user': request.user}
        return render(request, self.template_name, context=context)

class Jugar(View):

    template_name = 'partidas/tablero.html'

    def get(self, request, pk):
        partida = Partida.objects.get(pk=pk)
        tablero = Tablero.objects.get(partido__pk=pk)
        user = request.user
        context = {'partida': partida, 'tablero': tablero, 'user': user, 'jugador_actual_username': partida.jugador_x.username}
        return render(request, self.template_name, context=context)

class Partidas(View):

    template_name = 'partidas/tablero.html'

    def get(self, request):
        return render(request, self.template_name)

class Resultado(View):

    template_name = 'partidas/resultado.html'

    def get(self, request):
        return render(request, self.template_name)

class ResultadoPartida(View):

    template_name = 'partidas/resultadoPartida2.html'

    def get(self, request):
        return render(request, self.template_name)

class Rooms(View):

    template_name = 'partidas/rooms.html'

    def get(self, request):
        return render(request, self.template_name)
from django.shortcuts import render
from django.views.generic import View

# Create your views here.



class Partidas(View):

    template_name = 'partidas/tablero.html'

    def get(self, request):
        return render(request, self.template_name)



from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Estadisticas(View):

    template_name = 'stats/estadisticas.html'

    def get(self, request):
        return render(request, self.template_name)
from django.shortcuts import render
from django.views.generic import View


class Cargando(View):

    template_name = 'home/index.html'

    def get(self, request):
        return render(request, self.template_name)
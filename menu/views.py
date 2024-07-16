from django.shortcuts import render
from django.views.generic import View

# Create your views here.



class Menu(View):

    template_name = 'menu/menu.html'

    def get(self, request):
        return render(request, self.template_name)


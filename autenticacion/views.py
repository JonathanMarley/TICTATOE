from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout




class SignUp(View):

    template_name = 'autenticacion/sign-up.html'

    def get(self, request):
        return render(request, self.template_name)
    

class Login(View):

    template_name = 'autenticacion/sign-in.html'

    def get(self, request):
        return render(request, self.template_name)
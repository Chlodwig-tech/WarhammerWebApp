from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from utilities.authenticators import when_logged_in, when_logged_out
from .forms import RegisterForm, LoginForm
# Create your views here.

class RegisterView(View):

    @when_logged_out
    def get(self, request):
        form = RegisterForm()
        context = {
            'form' : form
        }
        return render(request, 'user_auth/register.html', context)
    
    @when_logged_out
    def post(self, request):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Rejsetracja nie udała się. Podano nieprawidłowe dane.')
            return redirect('.')
        user = form.save()
        login(request, user)
        messages.success(request, 'Rejestracja przebiegła pomyślnie')
        return redirect('/login')

    
class LoginView(View):
    
    @when_logged_out
    def get(self, request):
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, 'user_auth/login.html', context)
    
    @when_logged_out
    def post(self, request):
        form = LoginForm(request.POST, data=request.POST)
        if not form.is_valid():
            messages.error(request,"Nieprawidłowy login lub hasło.")
            return redirect('.')
        
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            print('Co?')
            messages.error(request,"Nieprawidłowy login lub hasło.")
            return redirect('.')

        login(request, user)
        messages.info(request, f"Jesteś zalogowany jako {username}.")
        return redirect('/welcome')

class LogoutView(View):

    @when_logged_in
    def get(self, request):
        logout(request)
        messages.info(request, "Wylogowałeś się pomyślnie.")
        return redirect('.')
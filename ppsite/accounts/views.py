from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.views import LoginView

def register(request):
    

    return render(request, 'accounts/register.html', {'form': form})


def login(request):

    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    
    return render(request, 'accounts/login.html', {'form': form})
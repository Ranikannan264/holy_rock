from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
import requests

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def jwt_login_view(request):
    error = ''
    next_url = request.GET.get('next', 'home')  

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  
            return redirect(request.POST.get('next', next_url))
        else:
            error = "Invalid username or password"

    return render(request, 'login.html', {'error': error, 'next': next_url})


def jwt_logout_view(request):
    logout(request)  
    return redirect('login')


def home_view(request):
    return render(request, 'home.html')
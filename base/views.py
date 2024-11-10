from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import User

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        name = request.POST.get('name')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            my_user = User.objects.create_user(email=email, username=name, password=password)
            my_user.save()
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login/')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

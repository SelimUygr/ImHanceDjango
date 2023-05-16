from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Assuming you have a model named Pictures in your models.py
from .models import Pictures

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        new_user = authenticate(request, username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return redirect('main')  # Make sure 'main' is a valid url name in your urls.py
    return render(request, 'register.html')

def login_view(request):  # Renamed function to avoid conflict with the built-in 'login' function
    if request.method == 'POST':
        username = request.POST['username']  # In Django, usually username is used for authentication instead of email
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Django's built-in authentication
        if user is not None:
            login(request, user)
            return redirect('main')  # Make sure 'main' is a valid url name in your urls.py
        else:
            return render(request, 'login.html', {'message': "Username or password incorrect!"})
    return render(request, 'login.html')

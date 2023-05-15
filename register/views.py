from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

from .models import User,Pictures
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        new_user = User(username=username,password=password,email=email)
        new_user.save()
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        if(not User.objects.filter(email=email,password=password).exists()):
            return render(request, 'login.html', {'message': "Username or password incorrect!"})
        else:
            return redirect("/")
    return render(request, 'login.html')

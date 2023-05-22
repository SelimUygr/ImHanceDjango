from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import ImHanceUser
import hashlib
# Create your views here.
def register(request):
    if request.POST:
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_password = hashlib.sha256(password.encode('utf-8')).hexdigest() # Hashing the password before store.
        user = ImHanceUser.objects.filter(email=email)
        if not user.exists():
          ImHanceUser.objects.create(name=name,surname=surname,email=email,password = user_password)
        else:
            return render(request,"registerPage.html",context={
                "status" : 409
            })
    return render(request,"registerPage.html")

def login(request):
    if request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_password = hashlib.sha256(password.encode('utf-8')).hexdigest() # Hashing the password before store.
        user = ImHanceUser.objects.filter(email=email)
        if user.exists():
            if user.values()[0]["password"] == user_password:
                user.update(logged = 1)
                return render(request,"mainPage.html",context={
                    "email" : email,
                    "name" :  user.values()[0]["name"]
                })
            else:
                return render(request,'loginPage.html',context={
                    "status" : 401,
                })
        else:
            return render(request,'loginPage.html',context={
                "status" : 401,
                "message" : "Email or password is invalid!"
            })
    return render(request,"loginPage.html")
    
def logout_user(request):
    email = request.email
    user = ImHanceUser.objects.filter(email=email)
    user.updaet(logged = 0)
    return render(request,"loginPage.html")
    
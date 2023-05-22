from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.register,name="RegisterPage"),
    path('logout',views.logout,name="LogoutPage"),
    path('',views.login,name="LoginPage"),
]

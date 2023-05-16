from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register, name='register'),
    path('', views.register, name='login'),
    # Add your other urls here
]

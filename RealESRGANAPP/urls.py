from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="MainPage"),
    path('enhance', views.enhance_image,name="ImageEnhancerFunction"),
]

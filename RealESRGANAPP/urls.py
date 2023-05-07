from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.enhance_image,name="ImageEnhancerFunction"),
]

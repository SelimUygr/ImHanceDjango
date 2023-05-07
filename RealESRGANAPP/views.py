from django.shortcuts import render
from . import inference_realesrgan
import os
# Create your views here.
def enhance_image(request):
    print(os.getcwd())
    image = request.FILES["lr_image"]
    context={
        'image': image,
    }
    return os.getcwd()
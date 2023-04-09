from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.conf import settings
import base64
import os
import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN

# Create your views here.
def index(request):
    template = loader.get_template("try.html")
    return HttpResponse(template.render())

def main(request):
    if request.method == 'POST':
        # Get the uploaded image file
        image_file = request.FILES.get('image_file', None)
        if not image_file:
            return JsonResponse({
                "status": False,
                "msg": "No image file provided",
            })

        # Convert the image file with the AI model
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = RealESRGAN(device, scale=4)
        model.load_weights('weights/RealESRGAN_x4.pth', download=True)
        image = Image.open(image_file).convert('RGB')
        sr_image = model.predict(image)
        sr_image.save(f'{settings.STATICFILES_DIRS[0]}/output.png')
        # Render a template that displays the converted image
        return render(request, 'result.html', {'image_path': 'static/output.png'})

    return render(request, 'try.html')

def result(request):
    image_path = f'{settings.STATICFILES_DIRS[0]}/output.png'
    print(image_path)
    return render(request, 'result.html', {'image_path': image_path})
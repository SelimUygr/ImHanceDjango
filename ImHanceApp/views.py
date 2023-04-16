from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def resize_image(image: Image.Image, max_size: int) -> Image.Image:
    width, height = image.size
    if max(width, height) > max_size:
        if width > height:
            new_width = max_size
            new_height = int(height * (max_size / width))
        else:
            new_width = int(width * (max_size / height))
            new_height = max_size
        return image.resize((new_width, new_height), Image.ANTIALIAS)
    return image


@csrf_exempt
def main(request):
    if request.method == 'POST':
        # Get the uploaded image file
        image_file = request.FILES.get('image_file', None)
        if not image_file:
            return JsonResponse({
                "status": False,
                "msg": "No image file provided",
            })

        # Check image dimensions
        image = Image.open(image_file).convert('RGB')
        width, height = image.size
        if width > 1980 or height > 1980:
            return JsonResponse({
                "status": False,
                "msg": "Image dimensions must not exceed 1980 pixels",
            })

        # Convert the image file with the AI model
        max_image_size = 500  # Adjust this value according to your desired maximum image size
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = RealESRGAN(device, scale=4)
        model.load_weights('weights/RealESRGAN_x4.pth', download=True)
        resized_image = resize_image(image, max_image_size)
        sr_image = model.predict(resized_image)
        sr_image.save(f'{settings.STATICFILES_DIRS[0]}/output.png')
        # Render a template that displays the converted image
        return render(request, 'result.html', {'image_path': 'static/output.png'})

    return render(request, 'try.html')

def result(request):
    image_path = f'{settings.STATICFILES_DIRS[0]}/output.png'
    print(image_path)
    return render(request, 'result.html', {'image_path': image_path})
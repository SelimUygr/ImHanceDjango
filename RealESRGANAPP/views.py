from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from . import inference_realesrgan
import base64
import cv2
# Create your views here.
def index(request):
    return render(request,'main.html')

def enhance_image(request):
    # Ensure there's a file and it's a POST request
    if request.method == 'POST' and 'image_file' in request.FILES:
        # Get the uploaded file
        image_file = request.FILES['image_file']

        # Save the file temporarily and get its path
        path = default_storage.save('tmp/' + image_file.name, ContentFile(image_file.read()))

        # Enhance image
        enhanced_image_base64 = inference_realesrgan.enhance(path)


        # Decode base64 bytes to string
        enhanced_image_str = enhanced_image_base64.decode()

        # Read the original image file
        with open(path, 'rb') as f:
            old_image_base64 = base64.b64encode(f.read()).decode()
            
        # After enhancing the image, delete the temporary file
        default_storage.delete(path)

        return render(request, 'result.html', {
            'image': enhanced_image_str,
            'old_image': old_image_base64
        })
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
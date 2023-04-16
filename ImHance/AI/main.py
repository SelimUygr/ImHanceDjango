import base64
import os
import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN

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

def main() -> int:
    max_image_size = 300  # Adjust this value according to your desired maximum image size
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGAN(device, scale=4)
    model.load_weights('weights/RealESRGAN_x4.pth')
    for i, image in enumerate(os.listdir("ImHance/AI/inputs")):
        image = Image.open(f"Imhance/AI/inputs/{image}").convert('RGB')
        resized_image = resize_image(image, max_image_size)
        sr_image = model.predict(resized_image)
        sr_image.save(f'Imhance/AI/results/{i}.png')

if __name__ == '__main__':
    main()

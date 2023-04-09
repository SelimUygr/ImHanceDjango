import base64
import os 
import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN

def main() -> int:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGAN(device, scale=4)
    model.load_weights('weights/RealESRGAN_x4.pth')
    for i, image in enumerate(os.listdir("ImHance/AI/inputs")):
        image = Image.open(f"Imhance/AI/inputs/{image}").convert('RGB')
        sr_image = model.predict(image)
        sr_image.save(f'Imhance/AI/results/{i}.png')


if __name__ == '__main__':
    main()
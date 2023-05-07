import cv2
import os

os.chdir(f"{os.getcwd()}/RealESRGANAPP")


import base64
from basicsr.archs.rrdbnet_arch import RRDBNet

from .realesrgan import RealESRGANer
# Change working directory to use ai model!

def enhance(img):
    #MODEL SETTINGS
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
    netscale = 4
    model_path = os.path.join('weights', 'RealESRGAN_x4plus.pth')

    # use dni to control the denoise strength
    dni_weight = 0.1
    
    # restorer
    upsampler = RealESRGANer(
        scale=netscale,
        model_path=model_path,
        dni_weight=dni_weight,
        model=model,
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=False,
        gpu_id=None)

    # Get image extension
    extension = (img.name.split('/'))[-1].split('.')[-1]

    # Read image with cv2 library
    img = cv2.imread(img.name, cv2.IMREAD_UNCHANGED)

    #Find the image type
    if len(img.shape) == 3 and img.shape[2] == 4:
        img_mode = 'RGBA'
    else:
        img_mode = None

    # Create an output img 
    output, _ = upsampler.enhance(img, outscale=4)

    if img_mode == 'RGBA':  # RGBA images should be saved in png format
        extension = 'png'

    # cv2.imencode(extension, output)[1]
    enhanced_image = base64.b64encode(cv2.imencode(f".{extension}", output)[1])

    return enhanced_image
img = open("inputs/image.png")
    
enhance(img)

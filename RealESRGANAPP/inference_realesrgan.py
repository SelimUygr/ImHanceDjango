import cv2
import os
import sys
import numpy as np
# Add project path to the system path for python to find all the modules in the project
sys.path.append(f"{os.getcwd()}/RealESRGANAPP")

# Change current working directory to the REALESRGANAPP directory for working in
os.chdir(f"{os.getcwd()}/RealESRGANAPP")


import base64
from basicsr.archs.rrdbnet_arch import RRDBNet

from realesrgan import RealESRGANer
# Change working directory to use ai model!

def enhance(img_path):
    # Read image with cv2 library
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

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
    filename = os.path.basename(img_path)
    name, extension = os.path.splitext(filename)
    extension = extension.lstrip('.')  # remove the leading dot

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
    enhanced_image = base64.b64encode(cv2.imencode(f".{extension}", output)[1].tobytes())
    return enhanced_image



# img = input("input b64 image: ")

# print(img)
# # img_64 = base64.b64encode(img)
# # print(img_64)
# enhance(img)

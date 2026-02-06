from PIL import Image
import os

def crop_father(image_path, output_path):
    with Image.open(image_path) as img:
        width, height = img.size
        # Focus on the left side where the father is
        # Crop a square from the left top
        size = min(width, height)
        # Shift a bit to the left to capture the father more
        left = 0
        top = 0
        right = size
        bottom = size
        
        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(output_path, "PNG")

if os.path.exists("папа.jpeg"):
    crop_father("папа.jpeg", "papa.png")
    print("Father's photo cropped successfully.")
else:
    print("папа.jpeg not found.")

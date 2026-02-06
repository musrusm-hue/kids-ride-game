from PIL import Image
import os

def crop_to_square(image_path, output_path):
    with Image.open(image_path) as img:
        width, height = img.size
        # Get dimensions for square
        min_dim = min(width, height)
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        
        # Special case for "папа.jpeg" to focus more on the left/top if needed
        # But generally center crop is a good start.
        
        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(output_path, "PNG")

files = {
    "жена.jpeg": "mama.png",
    "дети.jpeg": "deti.png",
    "папа.jpeg": "papa.png"
}

for src, dst in files.items():
    if os.path.exists(src):
        print(f"Cropping {src} to {dst}...")
        crop_to_square(src, dst)
    else:
        print(f"File {src} not found!")

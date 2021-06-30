import os
from PIL import Image

image_path = os.path.join(os.getcwd(), "images") 
image_list = os.listdir(image_path)
output_dir = os.path.join(os.getcwd(), "new_images")

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

if ".DS_Store" in image_list:
    image_list.remove(".DS_Store")


for image in image_list:
    with Image.open(os.path.join(image_path, image)) as im:
        im.convert('RGB').rotate(-90).resize((128, 128)).save(f"{os.path.join(output_dir)}/{image}.jpeg", "JPEG" )





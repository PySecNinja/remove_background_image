""""

Usage - Place images to remove the background in images folder. 
        Run this script 'python main.py' 
        See the removed background photos in results folder.

"""
from rembg import remove
from PIL import Image
import glob
import io

files = glob.glob("images/*.jpg")
print(files)

for file in files:
    input_path = file
    output_path = input_path.replace("images", "results")

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            original_image = i.read()
            output = remove(original_image)
            o.write(output)



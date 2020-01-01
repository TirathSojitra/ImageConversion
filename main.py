from PIL import Image, ImageFilter
import sys
import os

source = sys.argv[1]
dest = sys.argv[2]

path = r"./converted_images"

if not os.path.exists(path):
	os.makedirs(path)
	print("Sucess")
 
for file in os.listdir(source):
	filename = file.split(".")
	img = Image.open(f"./{source}/{file}")
	img.save(f"./{dest}/{filename[0]}.png")

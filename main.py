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
	#print(filename)
	img = Image.open(f"./{source}/{file}")
	img.save(f"./{dest}/{filename[0]}.png")













































# img = Image.open("./images/dragon.jpg")
#original_Image = img.convert("RBG")
# img.show()
# filtered_img = img.filter(ImageFilter.BLUR)
# bw_image = img.convert("L")
# filtered_img.save("fliter.png" , "png")
# bw_image.save("B_W.png" , "png")


# img = Image.open("./images/sp_needle.jpg")
# converted_img = img.resize((300,300))
# converted_img.show()
# img.show()
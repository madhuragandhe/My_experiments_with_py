#Python program to convert a photo to black and white
from PIL import Image

input_image = 'colored_we.png'
color_image = Image.open(input_image)
bw = color_image.convert('L')
bw.save('bw_we.png')

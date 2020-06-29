from PIL import Image

img= Image.open("Image\\sreach.png")
img= img.resize((25, 25), Image.ANTIALIAS)
img.save("Image\\serch25x25.png")
from PIL import Image
img= Image.open("Image\\Sign-Up.png")
img= img.resize((100, 50), Image.ANTIALIAS)
img.save("Image\\Sign-Up100x50.png")
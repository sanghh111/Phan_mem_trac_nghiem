from PIL import Image

img= Image.open("Image\\GenyTeam.png")
img= img.resize((800, 500), Image.ANTIALIAS)
img.save("Image\\GenyTeam50x50.png")
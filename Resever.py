from PIL import Image

img= Image.open("Image\\quizz.png")
img= img.resize((400, 400), Image.ANTIALIAS)
img.save("Image\\quizz400x400.png")
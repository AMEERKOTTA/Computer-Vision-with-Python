from PIL import Image
## Give the File Path ##
image = Image.open("H:\Files For Projects\Pictures\car10.jpg")
## Convert image to gray scale ##
image = image.convert("L")
## Show the Image ##
image.show()
from PIL import Image
## Give the File Path ##
image = Image.open("H:\Files For Projects\Pictures\car10.jpg")
## thumbnails ##
image.thumbnail((200,200))
## Show the Image ##
image.show()
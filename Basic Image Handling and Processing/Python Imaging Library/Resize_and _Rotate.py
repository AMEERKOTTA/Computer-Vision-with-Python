from PIL import Image

image = Image.open("H:\Files For Projects\Pictures\car10.jpg")

## Resize the Image ##
img_resize = image.resize((256,256))
## Rotate the Image ##
img_rotated = image.rotate(45)

## Show the Outputs ##
image.show()
img_resize.show()
img_rotated.show()
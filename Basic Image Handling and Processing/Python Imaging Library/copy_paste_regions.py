from PIL import Image
## Give the File Path ##
image = Image.open("H:\Files For Projects\Pictures\car10.jpg")
## Cropping a Region ##
box = (300,300,700,700)
region = image.crop(box)
## Rotate the Cropped Part ##
## Paste in the cropped and rotated part in the Image ##
region = region.transpose(Image.ROTATE_90)
image.paste(region,box)
## Show the Image ##
image.show()
region.show()
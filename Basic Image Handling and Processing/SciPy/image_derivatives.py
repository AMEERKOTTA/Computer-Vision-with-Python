from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

image = array(Image.open("H:\Files For Projects\Pictures\car9.jpg").convert("L"))

## sobel derivative filters ##
imageX = zeros(image.shape)
filters.sobel(image,1,imageX)

imageY = zeros(image.shape)
filters.sobel(image,0,imageY)

magnitude = sqrt(imageX**2 + imageY**2)


imshow(image)
show()
imshow(imageX)
show()
imshow(imageY)
show()
imshow(magnitude)
show()
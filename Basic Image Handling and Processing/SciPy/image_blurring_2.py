from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

image = array(Image.open("H:\Files For Projects\Pictures\car9.jpg"))
image2 = zeros(image.shape)
for i in range(3):
    image2[:,:,i] = filters.gaussian_filter(image[:,:,i],5)
image2 = uint8(image2)
image2 = array(image2, "uint8")

imshow(image)
imshow(image2)
show()

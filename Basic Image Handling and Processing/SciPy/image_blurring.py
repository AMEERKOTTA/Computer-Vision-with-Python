from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

image = array(Image.open("H:\Files For Projects\Pictures\car9.jpg").convert("L"))
img = filters.gaussian_filter(image,2)


imshow(image)
show()


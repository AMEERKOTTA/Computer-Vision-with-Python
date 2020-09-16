from PIL import Image
from pylab import *

## Read Image to Array ##
image = array(Image.open("H:\Files For Projects\Pictures\car9.jpg").convert("L"))

########### CONTOURS ##############

## Create a new figure ##
figure()
## don't use colors ##
gray()
## Show contours with origin upper left corner ##
contour(image,origin = "image")
axis("equal")
axis("off")
#show()

############### HISTOGRAM ###################

## histogram is a plot showing the distribution of pixel values ##
## hist() will give a histogram of grayscale image ##
## the second argument specifies the number of bins to use ##
## flatten() converts any array to a 1D array with values taken raw wise ##
figure()
hist(image.flatten(),128)
show()
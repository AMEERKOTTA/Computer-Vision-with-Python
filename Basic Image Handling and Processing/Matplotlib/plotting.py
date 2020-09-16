from PIL import Image
from matplotlib import pylab
from pylab import *

## Read Image to array ##
image = array(Image.open("H:\Files For Projects\Pictures\car10.jpg"))

## Plot the Image ##
imshow(image)

## Some Points ##
X = [100,100,400,400]
Y = [200,500,200,500]

## Plot the points with the red star-markers ##
plot(X,Y)         ## Default blue solid line ##
#plot(X,Y,"r*")   ## Red star markers ##
#plot(X,Y,"go-")  ## green line with circle markers
#plot(X,Y,"ks:")  ## black dotted line with square markers ##


## Line plot connecting the first two points ##
plot(X[:2],Y[:2])

## Add title and Show the Plot ##
title('Plotting: , "H:\Files For Projects\Pictures\car10.jpg"')
show()
axis("off")



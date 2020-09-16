from PIL import Image
from pylab import *

image = array(Image.open("H:\Files For Projects\Pictures\car9.jpg"))
imshow(image)
print("Please Click 3 Points")

## ginput() is used to mark points on images ##
x = ginput(3)
print("You Clicked:", x)
show()
from PIL import Image
import os

filelist = os.listdir(r"C:\Users\Wavicledata\Desktop\New folder")
for infile in filelist:

    outfile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("Cannot Convert", infile)
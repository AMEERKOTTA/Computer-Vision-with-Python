import os

path = r"C:\Users\Wavicledata\Desktop\New folder"

def get_imlist(path):
    """Returns a list of filenames for
    all jpg images in a Directory"""

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")]

print(get_imlist(path))
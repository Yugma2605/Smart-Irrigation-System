import os
from skimage import io

class image:

    def get_image():

        os.system("libcamera-still -o test.jpg")
        img = io.imread("test.jpg")
        return img
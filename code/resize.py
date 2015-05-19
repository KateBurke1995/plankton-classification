import glob
from scipy import ndimage
from scipy import misc
import numpy as np
import os

# Resize each image to a square with padding of 5 pixels at the boder
images =  glob.glob("*/*.jpg")
k = 0
for filename in images:
    pix=misc.imread(filename)
    M = max(pix.shape[0],pix.shape[1]) + 5
    padded_img = np.zeros((M,M))
    for i in range(0,M):
        for j in range(0,M):
            padded_img[i][j] = 255 #set it to zero to filp the colours

    dx = (M-pix.shape[0])/2 
    dy = (M-pix.shape[1])/2 

    for i in range(dx,dx+pix.shape[0]):
        for j in range(dy,dy+pix.shape[1]):
                padded_img[i][j] = pix[i-dx][j-dy]
                # padded_img[i][j] = 255 - padded_img[i][j] to filp images

    # # To creates new image 
    # misc.imsave(filename.split(".")[0]+'_p.jpg', padded_img)
    # following code will sremove old image
    misc.imsave(filename, padded_img)

# shopt -s globstar
# rm **/*_p*.jpg
# this will remove all resized images

import glob
from scipy import ndimage
from scipy import misc
import numpy as np
import os

# Code to created rotated images
images =  glob.glob("*/*.jpg")
dic = {}
for filename in images:
    
    pix=misc.imread(filename)

    flip_ud = np.flipud(pix)
    flip_lr = np.fliplr(pix)
    rotate_1 = ndimage.rotate(pix, 180)

    misc.imsave(filename.split(".")[0]+'_h.jpg', flip_ud)
    misc.imsave(filename.split(".")[0]+'_v.jpg', flip_lr)
    misc.imsave(filename.split(".")[0]+'_r.jpg', rotate_1)

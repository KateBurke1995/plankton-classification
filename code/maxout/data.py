import glob
from scipy import ndimage
from scipy import misc
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.transform import resize

def load_images(f_name_dir, img_dim=48):
    images = []
    filename = []
    dimensions = []
    
    for idx, filename in enumerate(f_name_dir[2]):
        img_name = "{0}{1}{2}".format(f_name_dir[0], os.sep, filename)         
        image = imread(img_name, as_grey=True)        
        images.append(image)
        filenames.append(filename)
        dimensions.append(image.shape)
        images = augument(images)
    return images, filenames, dimensions

def augument(images):
    aug_img = []
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
        aug_img.append(padded_img)
    return aug_img
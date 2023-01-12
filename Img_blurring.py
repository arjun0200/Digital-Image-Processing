import cv2   
import numpy as np
from matplotlib import pyplot as plt

# function for blur image
def blur(image):
    kernels=[3,5,9,13]
    for idx,k in enumerate(kernels):
        image_bl=cv2.blur(image,ksize=(k,k))
        cv2.imshow(str(k),image_bl)
        cv2.waitKey(0)

def resize(im,w,h):
    img = cv2.imread(im)
    cv2.imshow('Original',img)
    cv2.waitKey(0)
    # get dimensions of image
    dimensions = img.shape
    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    #height, width = img.shape[0:2]
    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)

    org_ht,org_wd =img.shape[0:2]
    print('width: ',org_wd)
    print('height: ',org_ht)

    new_image=cv2.resize(img, (height,width))
    return  im, new_image

    
#im, new_image= resize('Grains.jpg',600,400)
#cv2.imshow('RESIZED IMAGE', new_image)
#cv2.waitKey(0)
#blur(new_image)

#extract red channel: Format BGR-->0,1,2
img = cv2.imread('Grains.jpg')
green_channel = img[:,:,1]
blur(green_channel)
cv2.waitKey(0)

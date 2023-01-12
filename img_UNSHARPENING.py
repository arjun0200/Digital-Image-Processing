import cv2
import matplotlib.pyplot as plt
from scipy.ndimage.filters import median_filter
import numpy as np

#https://theailearner.com/2019/05/14/unsharp-masking-and-highboost-filtering/


# Load the image
#image = cv2.imread('unsharp_pasta.jpg')
# Load image as grayscale
image = cv2.imread('GRAIN_sharp.png', cv2.IMREAD_GRAYSCALE)
# Blur the image
gauss = cv2.GaussianBlur(image, (5,5), 0)
# Apply Unsharp masking # dst = alpha. image1 + beta.image2 + gamma
unsharp_image = cv2.addWeighted(image, 11, gauss, -10, 0)


plt.imshow(image, cmap='gray'), plt.axis("off")
plt.show()
plt.imshow(unsharp_image, cmap='gray'), plt.axis("off")
plt.show()

#Python: cv.AddWeighted(src1, alpha, src2, beta, gamma, dst) → None
#Parameters:	
#src1 – first input array.
#alpha – weight of the first array elements.
#src2 – second input array of the same size and channel number as src1.
#beta – weight of the second array elements.
#dst – output array that has the same size and number of channels as the input arrays.
#gamma – scalar added to each sum.
#dtype – optional depth of the output array; when both input arrays
#have the same depth, dtype can be set to -1,
#which will be equivalent to src1.depth().

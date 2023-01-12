import cv2
import numpy as np

import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt

# Load image as grayscale
image = cv2.imread('GRAIN_sharp.png', cv2.IMREAD_GRAYSCALE)

# Create kernel
kernel = np.array([[0, -1, 0], 
                   [-1, 5,-1], 
                   [0, -1, 0]])

# Sharpen image
image_sharp = cv2.filter2D(image, -1, kernel)

# Show image

plt.imshow(image, cmap='gray'), plt.axis("off")
plt.show()
plt.imshow(image_sharp, cmap='gray'), plt.axis("off")
plt.show()

#f = plt.figure()
#f.add_subplot(1,2, 1)
#plt.imshow(np.rot90(image,2))
#f.add_subplot(1,2, 2)
#plt.imshow(np.rot90(image_sharp,2))
#plt.show(block=True)


# Calculate the sharpened image
#sharp = image - 0.5*image_sharp

#plt.imshow(image, cmap='gray'), plt.axis("off")
#plt.show()
#plt.imshow(sharp, cmap='gray'), plt.axis("off")
#plt.show()





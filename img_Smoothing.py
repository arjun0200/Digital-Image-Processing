import cv2
import numpy as np
import matplotlib.pyplot as plt


# Import the image
img = cv2.imread('BIRD.jpg', 1)

# Define a function for plotting multiple figures
def plot_img(images, titles):
  fig, axs = plt.subplots(nrows = 1, ncols = len(images),
                          figsize = (20, 20))
  for i, p in enumerate(images):
    axs[i].imshow(cv2.cvtColor(p, cv2.COLOR_BGR2RGB))
    axs[i].set_title(titles[i])
    #axs[i].axis('off')
  plt.show()
  
# To show a side by side comparison of different filters with different kernel sizes.
for i in range(3,30,8):
  print("with kernel size: "+str(i))
  # Averaging filter
  a_img = cv2.blur(img,(i,i))

  # Gaussian Filter: Gaussian smoothing we take a weighted average of pixel
  #values in the neighborhood.
  g_img = cv2.GaussianBlur(img,(i,i),0)

  # Bilateral Filtering : Besides these spatial weights,
  #the bilateral filter adds a tonal weight
  #such that pixel values that are close to the pixel value in the
  #center are weighted more than pixel values that are more different.

  #This tonal weighting makes that the bilateral filter is capable
  #of preserving edges (large differences in tonal value)
  #while smoothing in the more flat regions (small tonal differences).
  #https://www.geeksforgeeks.org/python-bilateral-filtering/
  
  b_img = cv2.bilateralFilter(img,i,25,25)
  images=[img, a_img, g_img, b_img]
  titles=['original image',
          'box filter image',
          'gaussian filter image',
          'Bilateral filter image']
  plot_img(images, titles)

#cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, borderType]])
# src - input image
# d - Filter size. If it is non-positive, it is computed from sigmaSpace
# sigmaColor - Filter sigma in the color space (Range Filter)
# sigmaSpace - Filter sigma in the coordinate space (Domain Filter)

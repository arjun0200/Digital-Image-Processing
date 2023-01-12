import cv2
import numpy as np
import matplotlib.pyplot as plt
# Reading and Displaying the Image
# Import the image
image = cv2.imread('BIRD.jpg', 1)
cv2.imshow('Image',image) 
cv2.waitKey(0) #will display the window infinitely until any keypress




# Different Channels 
B, G, R = cv2.split(image) 

cv2.imshow("original", image) 

  
cv2.imshow("blue", B) 

  
cv2.imshow("Green", G) 

  
cv2.imshow("red", R) 

cv2.waitKey(0)
cv2.destroyAllWindows() 

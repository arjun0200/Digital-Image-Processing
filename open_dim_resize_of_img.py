import cv2 
from matplotlib import pyplot as plt 
# Reading and Displaying the Image 
image = cv2.imread('MRI-Brain.jpg') 
cv2.imshow('Image',image) 
cv2.waitKey(0) #will display the window infinitely until any keypress


# Know the dimension of an image 
h,w,c = image.shape 
print("Height of the image is ",h) 
print("Width of the image is ",w) 
print(c)

#  Know the pixel intensities inside a ROI and at specific locations
# ROI= image[110:190, 110:198] 
# print("Pixel intensity at ROI is: ") 
# print(ROI) 
Specific_Location = image[140,150] 
print("Pixel intensity at specific location is ",Specific_Location) 


#  Cropping the Image and Changing the size of an image #crop 
cropped_image = image[0:150, 0:150] 
cv2.imshow("Cropped Image", cropped_image) 
cv2.waitKey(0) 
#resize 
new_size = (int(w*0.5), int(h*0.5)) 
resized = cv2.resize(image, new_size) 
cv2.imshow("resized", resized) 
cv2.waitKey(0) 

h,w,c = resized.shape
print("Height of the resized image is ",h) 
print("Width of the resized  image is ",w) 
# 5. Display histogram 
histogram = cv2.calcHist([image],[0],None,[256],[0,256])
plt.plot(histogram) 
plt.show() 

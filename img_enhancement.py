
import cv2 
import numpy as np 
#from matplotlib import pyplot as pypt
import matplotlib.pyplot as plt

# 1.Reading and Displaying the Image 
img=cv2.imread('dark.jpg',0) #reading image #correction_image3.jpg, Correction2.jpg, Scene.jpg
cv2.imshow('Image',img) 
cv2.waitKey(0)


# 2.Know the dimension of an image 
dimensions = img.shape
print('Image Dimension    : ',dimensions)
#Image Dimension    :  (70, 105)



#Resizing
#resize  = cv2.resize(img, (210,140),interpolation = cv2.INTER_NEAREST)
resize  = cv2.resize(img, (320,480),interpolation = cv2.INTER_NEAREST)
cv2.imshow('resize', resize)
cv2.waitKey(0)
img=resize


#3.Histogram equalization Transformation:considers the global contrast of the image
eq=cv2.equalizeHist(img)
# stacking images side-by-side
res=np.hstack((img, eq))

#comparing input & output images side by side
cv2.imshow('Equalized Image',res)
#showing the comparision
plt.hist(img.ravel(),256,[0,256]) #plotting histogram for input image pypt.show() #showing histogram 
plt.hist(eq.ravel(),256,[0,256]) #plotting histogram for output image pypt.show() #showing histogram
plt.show() #showing histogram

cv2.waitKey(0)


#4.CLAHE (Contrast Limited Adaptive Histogram Equalization)
 #image is divided into small blocks called "tiles"
 #(tileSize is 8x8 by default in OpenCV).
# Then each of these blocks are histogram equalized as usual.
 #So in a small area, histogram would confine to a small region
 #(unless there is noise). If noise is there, it will be amplified.
 #To avoid this, contrast limiting is applied. If any histogram bin is
# above the specified contrast limit (by default 40 in OpenCV), those
# pixels are clipped and distributed uniformly to other bins before applying
# histogram equalization. After equalization,
# to remove artifacts in tile borders, bilinear interpolation is applied.

 #CLAHE operates on small regions in the image, called tiles, rather
# than the entire image. The neighboring tiles are then combined using
 #bilinear interpolation to remove the artificial boundaries.

# create a CLAHE object (Arguments are optional).

# The declaration of CLAHE  
# clipLimit -> Threshold for contrast limiting 
clahe = cv2.createCLAHE(clipLimit = 3 ) #clipLimit – This parameter sets the threshold for contrast limiting. The default value is 40.
final_img = clahe.apply(img) 
cv2.imshow("CLAHE image", final_img)
cv2.waitKey(0)


# stacking images side-by-side
res=np.hstack((eq, final_img))
#comparing input & output images side by side
cv2.imshow('Equalized vs CLAHE Image',res)



#Logarithmic Transformation: 

#img = cv2.imread('correction_image3.jpg',0) #reading image 
c = 255/(np.log(1 + np.max(img))) #log transformation
# Apply log transformation method 
output = np.log(img + 1) * c 
output = np.array(output, dtype = np.uint8) #int datatype 
#cv2.imshow('log_transformed.jpg', output) #showing image

#pypt.hist(img.ravel(),256,[0,256]) 
#pypt.show() 
#pypt.hist(output.ravel(),256,[0,256]) 
#pypt.show() 
# Display both images 

# stacking images side-by-side
res=np.hstack((img, output))

#comparing input & output images side by side
cv2.imshow('log_transformed Image',res)

cv2.waitKey(0)


#Power law transformation: 

#Give desired gamma value in the shell 
gvalue=float(input("Enter gamma value:")) 
#int datatype 
output = np.array(255*(img / 255) ** gvalue, dtype = np.uint8)  
#cv2.imshow("Gamma Transformation", output) #showing image
cv2.waitKey(0)
# stacking images side-by-side
res=np.hstack((img, output))

#comparing input & output images side by side
cv2.imshow('Gamma_transformed Image',res)


#plt.hist(img.ravel(),256,[0,256]) #plotting histograms pypt.show() 
#plt.hist(output.ravel(),256,[0,256]) 
#plt.show()

#plt.imshow(output, cmap='gray')
#plt.show()
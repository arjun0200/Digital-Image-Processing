import cv2 
image_1 = cv2.imread('BW1.png') 
image_2 = cv2.imread('BW2.png')




# 2.Know the dimension of an image 
dimensions = image_1.shape
print('Image Dimension    : ',dimensions)
#Image Dimension    :  (70, 105)




#Converting to Binary
img_grey = cv2.imread('BW1.png', cv2.IMREAD_GRAYSCALE)
# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128
# threshold the image 1
img_binary1 = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('BW image 1', img_binary1)
cv2.waitKey(0)
dimensions = img_binary1.shape
print('Image Dimension of BW image 1    : ',dimensions)
#Image Dimension    :  (70, 105)


# threshold the image 2
img_grey2 = cv2.imread('BW2.png', cv2.IMREAD_GRAYSCALE)
img_binary2 = cv2.threshold(img_grey2, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('BW image 2', img_binary2)
cv2.waitKey(0)
dimensions2 = img_binary2.shape
print('Image Dimension of BW image 2    : ',dimensions2)


image_1=img_binary1
image_2=img_binary2

#Resizing
resize1  = cv2.resize(image_1, (210,140),interpolation = cv2.INTER_NEAREST)
cv2.imshow('resize image 1', resize1)
cv2.waitKey(0)
resize2  = cv2.resize(image_2, (210,140),interpolation = cv2.INTER_NEAREST)
cv2.imshow('resize image 2', resize2)

cv2.waitKey(0)
image_1=resize1
image_2=resize2



#Performing AND Operation on both images 
result = cv2.bitwise_and(image_1, image_2, mask = None) 
cv2.imshow('AND',result) 
cv2.waitKey(0) 


#Performing OR Operation on both images 
result = cv2.bitwise_or(image_1, image_2, mask = None) 
cv2.imshow('OR',result) 
cv2.waitKey(0) 


#Performing XOR Operation on both images 
result = cv2.bitwise_xor(image_1, image_2, mask = None) 
cv2.imshow('XOR',result) 
cv2.waitKey(0)


#Performing NOT Operation on image 1 
result = cv2.bitwise_not(image_1, mask = None) 
cv2.imshow('NOT_1',result) 
cv2.waitKey(0) 


#Performing NOT Operation on image 2 
result = cv2.bitwise_not(image_2, mask = None) 
cv2.imshow('NOT_2',result) 
cv2.waitKey(0) 

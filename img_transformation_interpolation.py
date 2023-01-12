import cv2
import numpy as np

#img = cv2.imread('messi5.jpg')
img = cv2.imread('correction_image3.jpg',0)

# Scaling
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)#zooming
cv2.imshow('Image',img) 
cv2.waitKey(0)
cv2.imshow('zoom Image',res)
cv2.waitKey(0)
#OR

#height, width = img.shape[:2]
#res2 = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

#Translation
rows,cols =res.shape

M = np.float32([[1,0,50],[0,1,25]])
dst = cv2.warpAffine(res,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Rotation
rows,cols = res.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(res,M,(cols,rows))

cv2.imshow('res',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Affine: preserves lines and parallelism
#In affine transformation, all parallel lines in
#the original image will still be parallel in the output image.
#To find the transformation matrix, we need three points
#from input image and their corresponding locations in output image.
img = cv2.imread('label.jpg')
rows,cols,ch = img.shape

#pts1 = np.float32([[50,50],[200,50],[50,200]])
#pts2 = np.float32([[10,100],[200,50],[100,250]])


pts1 = np.float32([[80,124],[306,95],[390,427]])
#pts2 = np.float32([[80,124],[311,112],[333,437]])
#pts2 = np.float32([[80,124],[313,112],[324,447]])
pts2 = np.float32([[84,102],[305,96],[315,439]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

#cv2.imshow('Aff',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# stacking images side-by-side
res=np.hstack((img, dst))

#comparing input & output images side by side
cv2.imshow('OUTPUT',res)
cv2.waitKey(0)


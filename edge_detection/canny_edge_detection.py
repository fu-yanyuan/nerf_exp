import cv2
import numpy
from utils import rescale
# Read the original image
img_orgn = cv2.imread('./data/bunny/00000.png') 
img = rescale(img_orgn, 1)

# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# # Sobel Edge Detection
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=10) # Sobel Edge Detection on the Y axis
# sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# # Display Sobel Edge Detection Images
# cv2.imshow('Sobel X', sobelx)
# cv2.waitKey(0)
# cv2.imshow('Sobel Y', sobely)
# cv2.waitKey(0)
# cv2.imshow('Sobel X Y using Sobel() functAion', sobelxy)
# cv2.waitKey(0)

# Canny Edge Detection
canny = cv2.Canny(image=img_blur, threshold1=50, threshold2=100) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', canny)
cv2.waitKey(0)


dst = cv2.bitwise_not(canny)
cv2.imshow("inversed_img",dst)
cv2.waitKey(0)
# #display two images in a figure
# cv2.imshow("Edge detection by Canny", numpy.hstack([img_gray,canny]))
# cv2.waitKey(0)

cv2.destroyAllWindows()
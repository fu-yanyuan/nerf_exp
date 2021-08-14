import cv2 as cv
import os
import numpy as np

from utils import rescale

Folder = './data/bunny/'
SaveFolder1 = './data/bunny_sobel/'
SaveFolder2 = './data/bunny_canney/'
if not os.path.exists(SaveFolder1):
    os.makedirs(SaveFolder1)
if not os.path.exists(SaveFolder2):
    os.makedirs(SaveFolder2)

# print(os.listdir(Folder))  # this will return a list
for filename in os.listdir(Folder):
    file = cv.imread(os.path.join(Folder, filename))
    img = rescale(file, 1)
    img2 = img.copy()
    print(img.shape)

    # Convert to graycsale
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv.GaussianBlur(img_gray, (3,3), 0)

    # sobel
    sobelxy = cv.Sobel(src=img_blur, ddepth=cv.CV_8U, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    # print(sobelxy.shape)
    # cv.imshow('1',sobelxy)
    # cv.waitKey(0)
    
    sobelxy2 = cv.cvtColor(sobelxy, cv.COLOR_GRAY2BGR)
    print(sobelxy2.shape)
    sobelxy2 = cv.bitwise_not(sobelxy2)
    # cv.imshow('1',sobelxy2)
    # cv.waitKey(0) 
    SaveFile1 = SaveFolder1 + filename
    cv.imwrite(SaveFile1, sobelxy2)

    # sobelx64f = cv.Sobel(img_blur,cv.CV_64F,1,1,ksize=5)
    # print(sobelx64f.shape)
    # cv.imshow('1',sobelx64f)
    # cv.waitKey(0)


    # abs_sobel64f = np.absolute(sobelx64f)
    # sobel_8u = np.uint8(abs_sobel64f)
    # print(sobel_8u.shape)
    # cv.imshow('1',sobel_8u)
    # cv.waitKey(0)

    # sobelxy3 = cv.cvtColor(sobel_8u, cv.COLOR_GRAY2BGR)
    # print(sobel_8u.shape)
    # sobelxy3 = cv.bitwise_not(sobel_8u)
    # cv.imshow('1',sobelxy3)
    # cv.waitKey(0)



    # sobelxy2 = cv.cvtColor(sobelxy, cv.COLOR_GRAY2BGR)
    # sobelxy2 = cv.bitwise_not(sobelxy2)
    # SaveFile1 = SaveFolder1 + filename
    # cv.imwrite(SaveFile1, sobelxy)

    # Canny Edge Detection
    canny = cv.Canny(image=img_blur, threshold1=50, threshold2=100) # Canny Edge Detections
    canny = cv.bitwise_not(canny)
    canny = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
    SaveFile2 = SaveFolder2 + filename
    cv.imwrite(SaveFile2, canny)

    # print(canny.shape)
    # cv.imshow('img2',canny)

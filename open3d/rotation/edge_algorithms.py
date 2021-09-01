import cv2 as cv
import os
import numpy as np

from utils import rescale

def canny(ImageFolder, SaveFolder, r=1):
    if not os.path.exists(SaveFolder):
        os.makedirs(SaveFolder)
    
    for filename in os.listdir(ImageFolder):
        file = cv.imread(os.path.join(ImageFolder, filename))
        img = rescale(file, r)
        img2 = img.copy()
        print(img.shape)

        # Convert to graycsale
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # Blur the image for better edge detection
        img_blur = cv.GaussianBlur(img_gray, (3,3), 0)

        '''canney'''
        # Canny Edge Detection
        canny = cv.Canny(image=img_blur, threshold1=50, threshold2=100) # Canny Edge Detections
        canny = cv.bitwise_not(canny)
        canny = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
        SaveFile = SaveFolder + filename
        cv.imwrite(SaveFile, canny)
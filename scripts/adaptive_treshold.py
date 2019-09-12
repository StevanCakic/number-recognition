import sys
import cv2 as cv
from matplotlib import pyplot as plt
import os

IMAGES_FOLDER = sys.argv[1] # images read folder 
CONVERSION_METHOD = sys.argv[2] #th1, th2, th3
ROOT_FOLDER = ".\images" # write folder

for filename in os.listdir(IMAGES_FOLDER):
    # Image tresholding(preprocessing with adaptive filter)
    IMG = cv.imread(f'{IMAGES_FOLDER}\{filename}', 0)
    OUTPUT_LOCATION = ROOT_FOLDER + "\\adaptive\\" + filename
    IMG = cv.medianBlur(IMG, 1)
    if CONVERSION_METHOD == "th1": # Global Thresholding (v = 127)
        RET, TH = cv.threshold(IMG, 170, 255, cv.THRESH_BINARY)
    elif CONVERSION_METHOD == "th2": # 'Adaptive Mean Thresholding'
        TH = cv.adaptiveThreshold(IMG, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 4)
    elif CONVERSION_METHOD == "th3": # 'Adaptive Gaussian Thresholding'
        TH = cv.adaptiveThreshold(IMG, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    elif CONVERSION_METHOD == "th4": # Otsu's thresholding
        ret2, TH = cv.threshold(IMG, 250, 255, cv.THRESH_BINARY + cv.THRESH_OTSU) 
    elif CONVERSION_METHOD == "th5": # Otsu's thresholding after Gaussian filtering
        blur = cv.GaussianBlur(IMG, (5, 5), 0)
        ret3, TH = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    else:
        print("Invalid method")
        CONVERSION_METHOD = False
    if CONVERSION_METHOD:
        cv.imwrite(OUTPUT_LOCATION, TH)

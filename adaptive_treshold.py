import sys
import cv2 as cv
from matplotlib import pyplot as plt

IMG = cv.imread(sys.argv[1], 0)
IMG_NAME = f'{sys.argv[1][2:].split(".")[0]}_adaptive.jpg'

# Image tresholding(preprocessing with adaptive filter)

IMG = cv.medianBlur(IMG, 5)
ret, TH1 = cv.threshold(IMG, 127, 255, cv.THRESH_BINARY)
TH2 = cv.adaptiveThreshold(IMG, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
TH3 = cv.adaptiveThreshold(IMG, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11 , 2)

TITLES = ['Original Image', 'Global Thresholding (v = 127)', 
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

IMAGES = [IMG, TH1, TH2, TH3]

# Show results
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(IMAGES[i], 'gray')
    plt.title(TITLES[i])
    plt.xticks([]), plt.yticks([])

# plt.show()
IMG_LOCATION = IMG_NAME.split("\\")
OUTPUT_LOCATION = IMG_LOCATION[0] + "\adaptive\\" + IMG_LOCATION[1]
cv.imwrite(OUTPUT_LOCATION, TH1)

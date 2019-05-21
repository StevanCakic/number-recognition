import cv2 as cv
from matplotlib import pyplot as plt
import sys

img = cv.imread(sys.argv[1], 0)
img_name = f'{sys.argv[1][2:].split(".")[0]}_adaptive.jpg'

# Image tresholding(preprocessing with adaptive filter)
# https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html?fbclid=IwAR1u-zeXf_bWLRhCOsHnLDRBzEEsNoT9B0f5Ibmy5zXeQxSn8z5eclkfW-0
img = cv.medianBlur(img,5)
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11 , 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]

# Show results
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv.imwrite(img_name, th3)

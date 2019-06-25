import sys
import cv2
import os

# sys.argv[1] - image name which you converts to grayscaled version

IMAGES_FOLDER = sys.argv[1]
ROOT_FOLDER = ".\images"
for filename in os.listdir(IMAGES_FOLDER):
    image_path = f'{IMAGES_FOLDER}\{filename}'
    IMAGE = cv2.imread(image_path)
    GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)
    OUTPUT_LOCATION = ROOT_FOLDER + "\\gray\\" + filename
    cv2.imwrite(OUTPUT_LOCATION, GRAY)
import sys
import cv2

# sys.argv[1] - image name which you converts to grayscaled version
IMAGE = cv2.imread(sys.argv[1])
GRAY = cv2.cvtColor(IMAGE, cv2.COLOR_BGR2GRAY)
IMG_LOCATION = f'{sys.argv[1][2:].split(".")[0]}_gray.jpg'.split("\\")
OUTPUT_LOCATION = IMG_LOCATION[0] + "\gray\\" + IMG_LOCATION[1]
cv2.imwrite(OUTPUT_LOCATION, GRAY)
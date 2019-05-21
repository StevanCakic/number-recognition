import cv2
import sys

# sys.argv[1] - image name which you convert to gray version
image = cv2.imread(sys.argv[1])

img_name = f'{sys.argv[1][2:].split(".")[0]}_gray.jpg'

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(img_name, gray)
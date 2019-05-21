from PIL import Image
import cv2
import pytesseract
import sys

# This path stores location to to executable tesseract (maybe different on your machine)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

# https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
# Simple image to string

print(pytesseract.image_to_string(Image.open(sys.argv[1])))

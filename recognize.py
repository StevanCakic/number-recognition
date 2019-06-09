from PIL import Image
import pytesseract
import sys

# This path stores location to to executable tesseract (maybe different on your machine)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

# https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
# Simple image to string

str_serial_number = pytesseract.image_to_string(Image.open(sys.argv[1]), config='--psm 6')
digits = list(filter(str.isdigit, str_serial_number))
result = int("".join(digits))
print(result)

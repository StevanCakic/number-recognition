import sys
import os
from PIL import Image
import pytesseract

# This path stores location to to executable tesseract (maybe different on your machine)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

# https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc

def get_number_from_image_name(filename): 
    index_of_ = filename.find('_')
    index_of_dot = filename.find(".")
    new_filename = ""
    version = 1
    if index_of_ > -1:
        new_filename = filename[0:index_of_]
        version = filename[index_of_ + 1: index_of_dot]
    else:
        new_filename = filename[0:index_of_dot]
    
    return new_filename, version


def main(images):
    # We check if file name is the same as number which is recognized
    text = ""
    valid = 0
    num_of_images = len(os.listdir(images))

    # Loop over all images
    for filename in os.listdir(images):
        new_filename, version = get_number_from_image_name(filename)
        image_path = f'{images}\\{filename}'
        
        # Tesseract configuration, main part to set 
        serial_number = pytesseract.image_to_string(Image.open(image_path), lang='eng',
            config='--psm 10 --oem 1 -c tessedit_char_whitelist=0123456789')
        
        # Chech if char is digit, maybe this is redudant because of whitelisting
        digits = list(filter(lambda str: str.isdigit(), serial_number))

        # Create results string/number from image
        result = "".join(digits)

        # Check if number from filename same as tesseract recognized number
        if new_filename == result:
            valid += 1

        # Text to save in output file
        text += "Version:" + str(version) + ";Original:" + new_filename + ";Recognized:" + result + "\n"
    
    # Calculate perc of numbers which are recognized correct
    text += "Perc:" +  str((valid * 100) / num_of_images)

    # Store results to txt file
    with open("results.txt", "w", encoding="utf-8") as file:
        file.write(text)

if __name__ == "__main__":
    # set folder where images are stored
    IMAGES_FOLDER = sys.argv[1]
    main(IMAGES_FOLDER)

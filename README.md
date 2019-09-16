# Image preprocessing and text recognizer from image
Image preprocessing with adaptive filters

For better understanding adaptive treshhold read <a href="https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html?fbclid=IwAR1u-zeXf_bWLRhCOsHnLDRBzEEsNoT9B0f5Ibmy5zXeQxSn8z5eclkfW-0
" target="_blank">this article</a>

Used packages: <br>
- <a href="https://pypi.org/project/opencv-python/" target="_blank">Open CV</a> <br>
- <a href="https://pypi.org/project/pytesseract/" target="_blank">Tesseract</a> <br>

To use these image preprocess, first you should set environment and install required packages:<br>
- <b>pip install </b><br>
Also you need to install <a href="https://www.bl.uk/britishlibrary/~/media/bl/global/early%20indian%20printed%20books/training%20resources/installing%20and%20using%20tesseract%20ocr.pdf" target="_blank">Tesseract</a> on your machine

How to use scripts: <br>

- <b>images_preprocessing.py</b> -> Script preprocess image for recognizing script<br>
<b>python .\scripts\images_preprocessing.py .\images\serial_numbers</b> <br>

- <b>recognize.py </b> -> Script gets text from the image and store results.txt file <br>
You can call this script simply by calling this command in terminal: <br>
<b>python .\scripts\recognize.py .\images\preprocessed </b> <br>

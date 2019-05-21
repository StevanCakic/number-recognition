# images-preprocessing
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
- <b>to_gray.py </b> -> Script converts image to gray scaled image format. <br>
You can call this script simply by calling this command in terminal: <br>
<b>python to_gray.py <img_name></b> <br>
eg. python to_gray.py image.jpg -> output will be gray scaled image in same folder named image_gray.jpg<br>

- <b>adaptive_treshold.py</b> -> Script convert image to a black/white drawing (adaptive treshold) which is used to later for recongize script to easier recognize text from the image<br>
<b>python adaptive_treshhold.py <img_name></b> <br>
eg. python adaptive_treshold.py image.jpg -> output will be black/white drawing in same folder named image_adaptive.jpg<br>

- <b>recognize.py </b> -> Script gets text from the image and print that text in a terminal <br>
You can call this script simply by calling this command in terminal: <br>
<b>python recognize.py <img_name></b> <br>
eg. python recognize.py preprocessed.jpg -> output will recognized text from the image<br>
  



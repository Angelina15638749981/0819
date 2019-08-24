
import urllib.request
# urllib.request.urlretrieve('https://www.tcpjw.com/img/normalize/20190613/090017531.jpg', 'd.jpg')
import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'D:/softwares/tesseract/tesseract.exe'

text = pytesseract.image_to_string("ROI_hw1.png", lang='chi_sim')
print(text)

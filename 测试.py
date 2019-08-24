
import cv2
import numpy as np
import pytesseract
# img_f = cv2.imread('ROI_w4.png',0)

# pytesseract.pytesseract.tesseract_cmd = 'D:/softwares/tesseract/tesseract.exe'
# text1 = pytesseract.image_to_string(img_f, lang='chi_sim')  # 读取文字，此为默认英文
# print(text1)


# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:23:19 2019
将图片按照表格框线交叉点分割成子图片（传入图片路径）
@author: hx
"""

import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'D:/softwares/tesseract/tesseract.exe'
# import urllib.request
# urllib.request.urlretrieve('https://www.tcpjw.com/img/normalize/20190613/090017531.jpg', 'd.jpg')

img = cv2.imread('ROI_c15.png', 1)
x, y = img.shape[0:2]
image = cv2.resize(img, (int(2*y), int(2*x)))

# cv2.imwrite('ROI_hw11.png', image, )
cv2.imshow("二值化图片：", image)  # 展示图片

# 灰度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 二值化
binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
# ret,binary = cv2.threshold(~gray, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("二值化图片：", binary)  # 展示图片
cv2.waitKey(0)



text1 = pytesseract.image_to_string(image, lang='chi_sim')  # 读取文字，此为默认英文
print(text1)




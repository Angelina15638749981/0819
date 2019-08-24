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

img = cv2.imread('ROI_hw4.png', 1)
x, y = img.shape[0:2]
image = cv2.resize(img, (int(2*y), int(2*x)))


# 灰度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 二值化
binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
# ret,binary = cv2.threshold(~gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("二值化图片：", binary)  # 展示图片
cv2.waitKey(0)


rows, cols = binary.shape
scale = 40
# 识别横线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols // scale, 1))
eroded = cv2.erode(binary, kernel, iterations=1)
# cv2.imshow("Eroded Image",eroded)
dilatedcol = cv2.dilate(eroded, kernel, iterations=1)
# cv2.imshow("表格横线展示：", dilatedcol)
cv2.waitKey(0)

# 识别竖线
scale = 20
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows // scale))
eroded = cv2.erode(binary, kernel, iterations=1)
dilatedrow = cv2.dilate(eroded, kernel, iterations=1)
# cv2.imshow("表格竖线展示：", dilatedrow)
cv2.waitKey(0)

# 标识交点
bitwiseAnd = cv2.bitwise_and(dilatedcol, dilatedrow)
cv2.imshow("表格交点展示：", bitwiseAnd)
cv2.waitKey(0)
# cv2.imwrite("my.png",bitwiseAnd) #将二值像素点生成图片保存

# 标识表格
merge = cv2.add(dilatedcol, dilatedrow)
cv2.imshow("表格整体展示：", merge)
# cv2.imwrite('merge.png', merge, )
cv2.waitKey(0)

# 两张图片进行减法运算，去掉表格框线
merge2 = cv2.subtract(binary, merge)
# cv2.imshow("图片去掉表格框线展示：", merge2)
# cv2.imwrite('e.png', merge2, )
cv2.waitKey(0)


text1 = pytesseract.image_to_string(image, lang='chi_sim')  # 读取文字，此为默认英文
print(text1)




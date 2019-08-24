import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'D:/softwares/tesseract/tesseract.exe'

# photo_name=str(input("请输入矫正的图片名字："))
image = cv2.imread('c15.png', 1)


#二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
#ret,binary = cv2.threshold(~gray, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("cell", binary)
cv2.imwrite('binary.png', binary, )

cv2.waitKey(0)

rows,cols=binary.shape
scale = 40
#识别横线
kernel  = cv2.getStructuringElement(cv2.MORPH_RECT,(cols//scale,1))
eroded = cv2.erode(binary,kernel,iterations = 1)
#cv2.imshow("Eroded Image",eroded)
dilatedcol = cv2.dilate(eroded,kernel,iterations = 1)
# cv2.imshow("Dilated Image",dilatedcol)
# cv2.waitKey(0)

#识别竖线
scale = 20
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,rows//scale))
eroded = cv2.erode(binary,kernel,iterations = 1)
dilatedrow = cv2.dilate(eroded,kernel,iterations = 1)
# cv2.imshow("Dilated Image",dilatedrow)
# cv2.waitKey(0)

#标识交点
bitwiseAnd = cv2.bitwise_and(dilatedcol, dilatedrow)
# cv2.imshow("bitwiseAnd Image",bitwiseAnd)
# cv2.imwrite('biaodian.png', bitwiseAnd, )

# cv2.waitKey(0)
# cv2.imwrite("my.png",bitwiseAnd)

#标识表格
merge = cv2.add(dilatedcol,dilatedrow)
# cv2.imshow("add Image",merge)
# cv2.imwrite('biaoge.png', merge, )

cv2.waitKey(0)

#识别黑白图中的白色点
ws,hs = np.where(bitwiseAnd>0)
# print(xs)
# print(ys)
mylistw=[]
mylisth=[]

#通过排序，获取跳变的x和y的值，说明是交点，否则交点会有好多像素值，我只取最后一点
i = 0
myxs=np.sort(hs)
for i in range(len(myxs)-1):
    if(myxs[i+1]-myxs[i]>10):
        mylisth.append(myxs[i])
    i=i+1
mylisth.append(myxs[i])


i = 0
myys = np.sort(ws)
# print(mylistx)
# print(mylisty)

for i in range(len(myys)-1):
    if(myys[i+1]-myys[i]>10):
        mylistw.append(myys[i])
    i=i+1
mylistw.append(myys[i])
# hhhhhhhhhhhhhhhhhhh
print(mylistw, len(mylistw))
# wwwwwwwwwwwwwwwww
print(mylisth,len(mylisth))




# 银行承兑汇票情况1
if len(mylistw)<16 and len(mylisth)<15:
    ROI = image[mylistw[0]:mylistw[4], mylisth[0]:mylisth[-1]]
    print(mylistw[0],mylistw[4], mylisth[0],mylisth[-1])



# [h,w]
# H截取
# ROI = image[138:, 70:] #减去3的原因是由于我缩小ROI范围 1.1
# # ROI = image[161:, 70:] #减去3的原因是由于我缩小ROI范围2
# # ROI = image[184:, 70:] #减去3的原因是由于我缩小ROI范围3
# # ROI = image[225:, 70:] #减去3的原因是由于我缩小ROI范围4
# # ROI = image[248:, 70:] #减去3的原因是由于我缩小ROI范围5
# # ROI = image[299:, 70:] #减去3的原因是由于我缩小ROI范围6
# # ROI = image[327:, 70:] #减去3的原因是由于我缩小ROI范围7
# # ROI = image[395:, 70:] #减去3的原因是由于我缩小ROI范围8

# W截取
# ROI = image[138:, 142:] #减去3的原因是由于我缩小ROI范围 w1
# ROI = image[138:, 251:] #减去3的原因是由于我缩小ROI范围w2
# ROI = image[138:, 578:] #减去3的原因是由于我缩小ROI范围w3
# ROI = image[138:, 643:] #减去3的原因是由于我缩小ROI范围w4
# ROI = image[138:, 753:] #减去3的原因是由于我缩小ROI范围w5
# ROI = image[138:, 753:980] #减去3的原因是由于我缩小ROI范围w6

# 截取hw
# ROI = image[138:161, 142:251] #减去3的原因是由于我缩小ROI范围 hw1
# ROI = image[138:161, 252:578] #减去3的原因是由于我缩小ROI范围hw2
# ROI = image[161:184, 251:578] #减去3的原因是由于我缩小ROI范围hw3

# 第一种情况c
# [138, 161, 184, 225, 248, 299, 327, 395, 435, 476, 526, 549, 573, 646, 666] 15
# [70, 142, 251, 477, 495, 535, 556, 578, 643, 753, 980] 11
# h  第一，第五
# w 第一，最后
# ROI = image[138:248, 70:980]

# 第二种情况c1
# [184, 203, 220, 251, 268, 307, 329, 380, 411, 441, 480, 497, 516] 13
# [58, 113, 196, 446, 501, 584, 751] 7
# h 第一，第五
# w 第一，最后
# ROI = image[184:268, 58:751]

# # 第四种情况 c3
# #[158, 181, 217, 254, 277, 315, 338, 390, 418, 446, 483, 502, 521] 13
# [85, 178, 431, 496, 590, 768] 6
# h 第一，第五
# w 第一，最后
# ROI = image[158:277, 85:768]

# # 第五种情况 c4
# [158, 181, 217, 254, 277, 315, 338, 390, 418, 446, 483, 502, 521] 13
# [85, 178, 431, 496, 590, 768] 6
# h 第一，第五
# w 第一，最后
# ROI = image[158:277, 85:768]

# # 第7种情况 c6
# [158, 181, 217, 240, 263, 301, 324, 376, 404, 432, 469, 488, 507] 13
# [28, 85, 178, 431, 496, 590, 768] 7
# h 第一，第五
# w 第一，末一
# ROI = image[158:263, 28:768]

# # 第8种情况 c7
# [161, 178, 195, 212, 230, 267, 288, 325, 355, 385, 421, 439, 457] 13
# [104, 157, 238, 474, 527, 608, 776] 7
# h 第一，第五
# w 第一，末一
# ROI = image[161:230, 104:776]

# # 第9种情况 c8
# [158, 181, 217, 240, 263, 301, 324, 376, 404, 432, 469, 488, 507] 13
# [28, 85, 178, 431, 496, 590, 768] 7
# h 第一，第五
# w 第一，末一
# ROI = image[158:263, 28:768]

# # 第10种情况 c9
# [158, 181, 217, 254, 277, 315, 338, 390, 418, 446, 483, 502, 521] 13
# [85, 178, 431, 496, 590, 768] 6
# h 第一，第五
# w 第一，末一
# ROI = image[158:277, 85:768]


# # 第11种情况 c10
# [158, 181, 217, 254, 277, 315, 338, 390, 418, 446, 483, 502, 521] 13
# [85, 178, 431, 496, 590, 768] 6
# h 第一，第五
# w 第一，末一
# ROI = image[158:277, 85:768]


# # 第12种情况 c11
# [158, 181, 217, 240, 263, 301, 324, 376, 404, 432, 469, 488, 507] 13
# [28, 85, 178, 431, 496, 590, 768] 7
# h 第一，第五
# w 第一，末一
# ROI = image[158:263, 28:768]


# ------------------------------------------------------------------------------------------------------------------------
# 银行承兑汇票情况1
elif len(mylistw)>=16 and len(mylistw)>15:
    ROI = image[mylistw[1]:mylistw[4], mylisth[1]:mylisth[-1]]
    print(mylistw[1],mylistw[4], mylisth[1],mylisth[-1])
# 第三种情况c2
# [43, 137, 169, 195, 222, 248, 276, 304, 351, 377, 403, 450, 476, 513, 545, 566] 16
# [20, 100, 163, 286, 352, 377, 446, 468, 490, 512, 534, 556, 578, 600, 622, 644, 667, 689, 711, 790] 20
# h 第二，第五
# w 第二，末二
# ROI = image[137:222, 100:711]

# # 第6种情况 c5
# [38, 129, 160, 185, 216, 241, 266, 291, 322, 347, 372, 417, 442, 479, 515, 546, 570] 17
# [81, 108, 168, 213, 315, 339, 404, 428, 452, 476, 499, 523, 547, 571, 594, 618, 642, 666, 690, 726] 20
# h 第二，第五
# w 第二，末二
# ROI = image[129:216, 108:690]

# # 第13种情况 c12
# [75, 169, 190, 210, 230, 250, 272, 295, 315, 335, 355, 385, 405, 434, 463, 532] 16
# [68, 108, 163, 223, 368, 397, 459, 479, 497, 515, 532, 550, 568, 586, 604, 622, 640, 658, 678, 740] 20
# h 第二，第五
# w 第二，末二
# ROI = image[169:230, 108:678]


#
# hwi
photo_name = str(input("请输入HW的图片名字："))
cv2.imwrite('ROI_%s.png' % photo_name, ROI, )
cv2.imshow("Cut Image", ROI)
cv2.waitKey(0)
text = pytesseract.image_to_string(ROI, lang='chi_sim')  #读取文字，此为默认英文
print(text)
# 测试 ROI_c13
# # [59, 203, 221, 240, 259, 299, 322, 376, 408, 441, 481, 500, 518, 548] 14
# # [14, 99, 187, 442, 500, 588, 770, 793] 8
# # 59 259 14 793
# 测试 ROI_c14
# [59, 203, 221, 240, 259, 299, 322, 376, 408, 441, 481, 500, 518, 548] 14
# [14, 99, 187, 442, 500, 588, 770, 793] 8
# 59 259 14 793
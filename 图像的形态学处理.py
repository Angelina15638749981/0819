import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'D:/softwares/tesseract/tesseract.exe'
#
img = cv2.imread('c.png', 0)
# 先对图像进行一个二值化处理
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# 用numpy定义结构元素
npKernel = np.uint8(np.zeros((5, 5)))
for i in range(5):
    npKernel[2, i] = 1
    npKernel[i, 2] = 1
print(npKernel)
# 用OpenCV中的getStructuringElement()函数定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# 进行腐蚀操作
npKernel_eroded = cv2.erode(th2, npKernel)
kernel_eroded = cv2.erode(th2, kernel)
cv2.imshow('img', th2)
# cv2.imshow('npKernel Eroded Image', npKernel_eroded)
# cv2.imshow('kernel Eroded Image', kernel_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

#
#
#
# img = cv2.imread('c.png', 0)
# # 先对图像进行一个二值化处理
# ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# # 用numpy定义结构元素
# npKernel = np.uint8(np.zeros((5, 5)))
# for i in range(5):
#     npKernel[2, i] = 1
#     npKernel[i, 2] = 1
# # 用OpenCV中的getStructuringElement()函数定义结构元素
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# # 进行膨胀操作
# npKernel_dilated = cv2.dilate(th2, npKernel)
# kernel_dilated = cv2.dilate(th2, kernel)
# # cv2.imshow('img', th2)
# # cv2.imshow('npKernel Dilated Image', npKernel_dilated)
# # cv2.imshow('kernel Dilated Image', kernel_dilated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# # 开运算操作
# img = cv2.imread('c.png', 0)
# ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# for i in range(2000):  # 添加椒盐噪声
#     _x = np.random.randint(0, th2.shape[0])
#     _y = np.random.randint(0, th2.shape[1])
#     th2[_x][_y] = 255
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)  # 开运算函数
# # cv2.imshow('th2', th2)
# # cv2.imshow('morph_open', erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# # 闭运算
# img = cv2.imread('c.png', 0)
# ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# for i in range(20000):  # 添加椒盐噪声
#     _x = np.random.randint(0, th2.shape[0])
#     _y = np.random.randint(0, th2.shape[1])
#     th2[_x][_y] = 0
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel)
# # cv2.imshow('th2', th2)
# # cv2.imshow('erosion', erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # 形态学梯度
# img = cv2.imread('c.png', 0)
# ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# kernel = np.ones((5, 5), np.uint8)
# # morphology  形态学
# gradient = cv2.morphologyEx(th, cv2.MORPH_GRADIENT, kernel)  # morph gradient 形态梯度
# cv2.imshow('th', th)
# cv2.imwrite("xingtaixue.png",th) #将二值像素点生成图片保存
#
# # cv2.imshow('gradient', gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

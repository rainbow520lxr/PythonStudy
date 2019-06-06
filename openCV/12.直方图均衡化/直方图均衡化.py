import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
直方图均衡化
首先必须将其变为灰度图
加强其对比度效果，分散灰度级
'''

'''全局直方图均衡化'''
def equalHist(win, img):
    gray = cv.cvtColor((img, cv.COLOR_BGR2GRAY))
    dst = cv.equalizeHist(img)
    cv.imshow(win, dst)

'''局部直方图均衡化'''
def claheHist(win, img):
    gray = cv.cvtColor((img, cv.COLOR_BGR2GRAY))
    clahe = cv.createCLAHE(5, (8, 8))
    dst = clahe.apply(gray)
    cv.imshow(win, dst)




if __name__ == '__main__':
    print("- - - - - - - - - - - - Hello Python - - - - - - - - - - - - -")
    cv.namedWindow("img1", 0)
    cv.resizeWindow("img1", 500, 500)
    cv.namedWindow("img2", 0)
    cv.resizeWindow("img2", 500, 500)
    src = cv.imread(r"D:/img/girl/ban.jpg")
    cv.imshow("img1", src)
    equalHist("img1", src)
    cv.waitKey(0)
    cv.destroyAllWindows()
import cv2 as cv

'''对两个相同维度的矩阵进行相加'''
def add(image1, image2):
    dst = cv.add(image1, image2)
    cv.imshow("add, dst")

'''对两个相同唯独的矩阵进行相减'''
def subtract(image1, image2):
    dst = cv.subtract(image1, image2)
    cv.imshow("subtract", dst)

'''对两个相同唯独的矩阵进行相除'''
def divide(image1, image2):
    dst = cv.divide(image1, image2)
    cv.imshow("divide", dst)

'''对两个相同唯独的矩阵进行相乘'''
def multiply(image1, image2):
    dst = cv.multiply(image1, image2)
    cv.imshow(dst)

def other(image1, image2):
    '''求均值'''
    mean1 = cv.mean(image1)
    mean2 = cv.mean(image2)
    '''求均值和标准方差'''
    m1, dev1 = cv.meanStdDev(image1)
    m2, dev2 = cv.meanStdDev(image2)
    ''''''
    

import cv2 as cv
import numpy as np

'''
边缘保留滤波EPF

'''

def bi(window, image):
    dst = cv.bilateralFilter(image, 0, 100, 20)
    cv.imshow(window, dst)

def shift(window, image):
    dst = cv.pyrMeanShiftFiltering(image, 3, 50)
    cv.imshow(window, dst)

'''均值模糊'''
if __name__ == '__main__':
    print("- - - - - - - - - - - - Hello Python - - - - - - - - - - - - -")
    cv.namedWindow("img1", 0)
    cv.resizeWindow("img1", 500, 500)
    cv.namedWindow("img2", 0)
    cv.resizeWindow("img2", 500, 500)
    src = cv.imread(r"D:/img/girl/ban.jpg")
    cv.imshow("img1", src)
    shift("img2", src)
    cv.waitKey(0)
    cv.destroyAllWindows()
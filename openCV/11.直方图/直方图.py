import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
统计直方图

'''


def img_hist(img):

    color = ("blue", "green", "yellow")
    for i,color in enumerate(color):
        hist = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim(([0, 256]))
    plt.show()


if __name__ == '__main__':
    print("- - - - - - - - - - - - Hello Python - - - - - - - - - - - - -")
    cv.namedWindow("img1", 0)
    cv.resizeWindow("img1", 500, 500)
    cv.namedWindow("img2", 0)
    cv.resizeWindow("img2", 500, 500)
    src = cv.imread(r"D:/img/girl/ban.jpg")
    cv.imshow("img1", src)
    img_hist(src)
    cv.waitKey(0)
    cv.destroyAllWindows()
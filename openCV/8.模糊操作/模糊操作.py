import cv2 as cv
import numpy as np
'''
模糊操作  使用 滤波 卷积核

椒盐噪声: 椒盐噪声，椒盐噪声又称脉冲噪声，它随机改变一些像素值，是由图像传感器，传输信道，解码处理等产生的黑白相间的亮暗点噪声。
椒盐噪声往往由图像切割引起。

'''

'''
均值模糊
作用：去掉图像的噪声
'''


def blur(window, image):
    dst = cv.blur(image, (2, 2))  #一行三列的卷积核
    cv.imshow(window, dst)


'''
中值模糊
作用去掉图像的椒盐噪声
'''


def median_blur(window, image):
    dst = cv.medianBlur(image, 5)
    cv.imshow(window, dst)


'''自定义模糊'''


def custom(window, image):
    kernel = np.ones([5, 5], np.float)/25
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow(window, dst)


'''均值模糊'''
if __name__ == '__main__':
    print("- - - - - - - - - - - - Hello Python - - - - - - - - - - - - -")
    cv.namedWindow("img1", 0)
    cv.resizeWindow("img1", 500, 500)
    cv.namedWindow("img2", 0)
    cv.resizeWindow("img2", 500, 500)
    src = cv.imread(r"D:/img/noise/jiaoyan.jpg")
    cv.imshow("img1", src)
    custom("img2", src)
    cv.waitKey(0)
    cv.destroyAllWindows()

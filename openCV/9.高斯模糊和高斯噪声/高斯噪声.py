'''
高斯噪声在于其随机性
'''

import cv2 as cv
import numpy as np


def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


def gaosi_noise(win, img):
    h, w, c = img.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)   # 参数：正态分布  均值， 方差， 输出的shape
            b = img[row, col, 0]   #blue
            g = img[row, col, 1]   #green
            y = img[row, col, 2]   #yellow
            img[row, col, 0] = clamp(b+s[0])
            img[row, col, 1] = clamp(g+s[1])
            img[row, col, 2] = clamp(y+s[2])
    cv.imshow(win, img)


def main():
    src = cv.imread(r"D:\img\dog\1.jpg")
    cv.namedWindow("origin", 0)
    cv.resizeWindow("origin", 500, 500)
    cv.imshow("origin", src)
    cv.namedWindow("res", 0)
    cv.resizeWindow("res", 500, 500)
    gaosi_noise("res", src)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()


import cv2 as cv
import numpy as np
def extrace_object_demo():
    captrue = cv.VideoCapture("../张杰-我是来揍你的 (《叶问外传：张天志》电影主题曲)(蓝光).mp4")
    while(True):
        ret, frame = captrue.read()
        '''判断'''
        if ret == False:
            break
        '''追踪视频的目标颜色'''
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([0, 43, 46])
        upper_hsv = np.array([10, 255, 255])
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)
        cv.imshow("video", frame)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            break

extrace_object_demo()
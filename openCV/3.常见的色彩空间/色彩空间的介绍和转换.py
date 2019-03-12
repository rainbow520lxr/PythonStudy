import cv2 as cv

'''色彩空间介绍'''
'''
RGB:对于RGB的色彩空间是立方体的色彩空间 三通道 红 黄 蓝 每个灰度级为255
HSV:对于HSV的色彩空间是255度的圆柱体 三通道 高度 圆心角 半径分别是255
HIS
YCrCb
YUV

'''
'''常用的色彩空间转换函数***cvtColor'''
def colorSpaceConvert(image):
    '''转换到灰度空间'''
    res = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", res)
    '''转换到HSV色彩空间'''
    res = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", res)
    '''转换到YUV色彩空间'''
    res = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", res)

image = cv.imread("../girl.jpg")
colorSpaceConvert(image)
'''等待下一个操作的延迟'''
cv.waitKey(0)
'''程序操作结束要销毁所有的窗口'''
cv.destroyAllWindows()
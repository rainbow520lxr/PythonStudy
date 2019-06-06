''''''
'''cv模块导入'''
import cv2 as cv
import numpy as np


'''视频的读取'''
def getVedio():
    '''初始化硬件摄像头对象，0代表第一个设备'''
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break

'''查看图片属性'''
def getImageInfo(image):
    print(type(image))
    print(image.shape) #高维度，宽维度，通道
    print(image.size) #多少字节
    print(image.dtype)  #编码
    pixelData = np.array(image)
    print(pixelData)

'''1.图像的读取'''
src = cv.imread(r"C:\Users\lxr\Desktop\girl.jpg")
'''2.创建一个GUI显示'''
cv.namedWindow("inputimage", cv.WINDOW_AUTOSIZE)
cv.namedWindow("inputimage", 0)
'''调整窗口大小'''
cv.resizeWindow("inputimage", 640, 480);
'''3.显示图片窗口'''
cv.imshow("inputimage", src)

'''获取灰度图'''
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

'''获取图片属性'''
getImageInfo(gray)
'''保存图片'''
cv.imwrite("demo.png",gray)
'''打开摄像机'''
getVedio()

'''4.等待下一个用户操作'''
cv.waitKey(0)
'''5.销毁'''
cv.destroyAllWindows()

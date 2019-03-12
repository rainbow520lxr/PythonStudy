import cv2 as cv
import numpy as np
'''像素点操作'''
def accessPixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("height : %s, width : %s, channel : %s"%(height, width, channels))
    '''对每一行每一列每一个通道的像素点进行像素操作，反转'''
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("girl", image)

'''像素反转cv的api这些api是用c语言写的可以大大节约时间，可以代替以上代码'''
def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse", image)

'''图像的创建,对与numpy矩阵可以常用使用0矩阵和1矩阵来初始化矩阵'''
def createImage():
    '''生成一个3通道的图像,像素是八位的'''
    image = np.zeros([400, 400, 3], np.uint8)
    '''初始化第一个通道的值'''
    image[:, :, 0] = np.ones([400, 400]) * 255
    '''初始化第二个通道的值'''
    image[:, :, 1] = np.ones([400, 400]) * 127
    '''初始化第三个通道的值'''
    image[:, :, 2] = np.ones([400, 400]) * 127
    cv.imshow("Image", image)
    '''生成一个单通道的图像'''
    image = np.ones([400, 400, 1], np.uint8)
    image = image * 255
    cv.imshow("Image1", image)

    m1 = np.ones([3, 3], np.uint8)
    m1.fill(122222.388)
    print(m1)

    m2 = m1.reshape([1, 9])
    print(m2)

print("- - - - - - - - - - - - Hello Python - - - - - - - - - - - -")
src = cv.imread(r"C:\Users\lxr\Desktop\girl.jpg")
# cv.namedWindow("input", cv.WINDOW_AUTOSIZE)

t1 = cv.getTickCount()
accessPixels(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time ：%ss" % (time))
createImage()
cv.waitKey(0)
cv.destroyAllWindows()
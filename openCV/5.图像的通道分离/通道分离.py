import cv2 as cv
src = cv.imread("../girl.jpg")
'''通道分离'''
b, g, r = cv.split(src)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)
'''将图片的3通道置为0'''
src[:, :, 2] = 0
cv.imshow("image", src)
src = cv.merge([b, g, r])
'''将图片通道合并'''
cv.imshow("merge", src)
cv.waitKey(0)
cv.destroyAllWindows()


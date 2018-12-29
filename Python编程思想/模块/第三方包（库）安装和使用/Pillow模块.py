#使用这个模块
from PIL import Image

#打开图片
im = Image.open("111.jpg")

#查看图片信息
print(im.format, im.size, im.mode)

#设置图片的大小
im.thumbnall(150, 100)

#保存成新图片
im.save("temp.jpg", "JPEG")
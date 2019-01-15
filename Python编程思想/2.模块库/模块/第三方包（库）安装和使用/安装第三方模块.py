''''''
'''
Mac:
Linux:
windows:安装python3自动安装了pip和add python.exe to Path


#要安装三方模块，需要知道模块的名字
Pillow 非常强大的处理图像的工具库
pip3 install Pillow
windows报错，则输入pip3 install --upgrade pip3升级

使用这个模块 
from PIL import Image

#打开图片
im = Image.open("111.jpg"

#打开图片的信息
print(im.format, im.size, im.mode)


'''
''''''
'''
OS;包含了普遍的操作系统的功能
'''

#第一步
import os

#可以获取操作系统的类型  nt->windows   posix->linux unix  Max OS X
print(os.name)

#打印操作系统的详细信息（windows不支持）
print(os.uname())

#获取操作系统的环境变量    环境变量：定义命令为系统命令，快捷定义命令-路径
print(os.environ)

#获取指定的环境变量
print (os.environ.get("APPDATA"))

#也可以修改环境变量

#获取当前目录  ./a/
print(os.curdir)

#获取当前工作目录，即当前python.py脚本所在的目录
print(os.getacwd())

#以列表的形式返回指定目录下的所有的文件，文件包括目录文件和文本文件
print(os.listdir(r"D:\IeHistory"))

#在当前目录下创建新目录
os.mkdir("sunck")
#在绝对路径下创建新目录
os.mkdir(r"D:\IeHistory")
#在相对路径删除文件
os.rmdir("sunck")
#在绝对路径下删除文件
os.rmdir(r"D:\IeHistory")

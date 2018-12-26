#有些方法存在os模块中，还有些存在于os.path
#查看当前的绝对路径
print(os.path.abspath("./kaige"))#括号内是相对路径

#路径的拼接
p1 = r"C:\user\lxr"
p2 = "git"
#注意：参数2里开始不要有斜杠
#r"C:\user\lxr"
print(os.path.join(p1, p2))

#拆分路径,拆最后的
path2 = r"C:\user\lxr"
print(os.path2.split(path2))
#拆分路径,拆最后的扩展名
path2 = r"C:\user\lxr\a.txt"
print(os.path2.splitext(path2))

#判断是否为目录
print(os.path.isdir(path2))

#判断文件是否存在
print(os.path.isfile(path2))

#判断目录是否存在
path2 = r"C:\user\lxr\a.txt"
print(os.path.exists(path))

#获得文件大小
print(os.path.getsize(path3))

#获得文件的目录
print (os.path.dirname(path3))
#获取文件的基本路径
print(os.basename(path3))
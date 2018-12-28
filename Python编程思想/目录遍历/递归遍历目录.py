import os
def getAllDir(path, sp = ""):
    #得到当前目录下所有的文件
    fileList = os.listdir(path)
    #遍历目录的分支
    # 显示目录层级
    sp += "     "

    for fileName in fileList:

        #这里的判断需要一个绝对路径
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录:", fileName)
            #递归调用
            getAllDir(fileAbsPath, sp)
        else:
            print(sp + "普通文件:", fileName)


getAllDir(r"C:\Users\lxr\Desktop\PythonStudy\Python编程思想")
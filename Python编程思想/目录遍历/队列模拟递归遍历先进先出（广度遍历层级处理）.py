import os
import collections

def getAllDirQU(path):
    #创建空队列
    queue = collections.deque()
    #进队
    queue.append(path)

    while len(queue) != 0:
        #出队列
        dirpath = queue.popleft()
        #处理：获取该目录文件下的目录
        filesList = os.listdir(dirpath)

        for fileName in filesList:
            #更改为绝对路径
            fileAbsPath = os.path.join(dirpath, fileName)

            if os.path.isdir(fileAbsPath):
                print("目录文件:", fileName)
                #入队
                queue.append(fileAbsPath)

            else:
                print("普通文件:", fileName)

getAllDirQU(r"C:\Users\lxr\Desktop\PythonStudy\Python编程思想")

#二叉树的栈的深度遍历

import os
def getAllDirDE(path):
    stack = []
    #压栈
    stack.append(path)

    #处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        #从栈里取出数据
        dirPath = stack.pop()
        #处理：获取目录下所有文件
        filesList = os.listdir(dirPath)

        #处理每一个问题，如果是普通文件则打印出来，如果是目录则将该目录的地址压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                #是目录就压栈
                print("目录:", fileName)
                stack.append(fileAbsPath)
            else:
                #打印普通文件
                print("普通文件:", fileName)


getAllDirDE(r"C:\Users\lxr\Desktop\PythonStudy\Python编程思想")
''''''
'''
from ...import语句
语句：从模块中导入一个指定的部分到当前命名空间

#格式: from module import name1[,name2[,....namen]]


'''
from template import sayGood

'''
程序内部的函数可以将模块中的同名函数覆盖
'''
def sayGood():
    print("###############")

sayGood()
template.sayGood()
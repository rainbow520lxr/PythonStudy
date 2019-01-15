''''''
'''
概念：调用函数时，如果没有传递参数，则使用默认参数

'''
'''使用默认参数，最好将默认参数放到最后
'''
def myPrint(str, age=10):
    print(str, age)
    
myPrint("lxr")

myPrint("lxr",18)
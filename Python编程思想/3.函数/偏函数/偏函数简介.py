''''''
'''
偏函数，对参数的控制
'''
print(int("1010", base = 2)) #


#自己定义一个偏函数,将函数需要固定的参数设置为关键字参数，即默认参数
def int2(str, base = 2):
    return int(str, base = 2 )

import functools
int3 = functools.partial(int, base = 2)#固定住一个参数,利用函数工具自动做一个偏函数
print(int3("111"))

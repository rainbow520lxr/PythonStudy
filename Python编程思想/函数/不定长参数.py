''''''
'''
概念：能处理比定义时更多的参数

'''
'''
加了星号（*)的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，
它就是一个空元组
'''
def fun(name, *arr):
    print(name)
    for x in arr:
        print(x)

fun("lxr", "sdd", "sdd", "sds", "sddw")

#求多项式的和，不确定有多少个参数

'''
**kwargs代表的是健值对的参数字典，和*所代表的意思类似
**后面值得是字典,该字典很特殊是{变量名：值，变量名：参数}
'''
def fun1(**kwargs):
    print(kwargs)
    print(type(kwargs))

fun1(x="asd",y="asd")

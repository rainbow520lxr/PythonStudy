''''''
'''
概念：是一个闭包，把一个函数当做参数返回一个替代版的函数，本上就是一个返回函数的函数

装饰器：函数内部本身不能修改，或着别人的函数不能修改时用装饰器来装饰
借鉴别人的源码时可以用装饰器添加自己想要的功能
'''

'''简单的装饰器
'''

def fun1():
    print("lxr is a good man!")

def outer(fun):   #把一个函数当作参数去装饰，outer装饰器
    def inner():  #替换的函数
        print("*****************")
        fun()
    return inner   #返回替代的函数

#f是函数fun1的装饰结果
f = outer(fun1)
f()

'''复杂装饰器
'''
def say(age):
    print("lxr is %d years old" % (age))

say(-10)

#开始写一个装饰say的装饰器
def outer(fun):
    def inner(age):
        if age < 0:
            age = 0
        fun(age)
    return inner

say = outer(say)
say(-10)
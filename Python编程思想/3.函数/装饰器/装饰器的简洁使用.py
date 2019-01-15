#在函数前面先写好装饰器
def outer(fun):
    def inner(age):
        if age < 0:
            age = 0
        fun(age)
    return inner

#可以使用@符号将装饰器应用到函数
#python2.4开始可以用
@outer #相当于say = outer(say)
def say(age):
    print("lxr is %d years old" % (age))

say(-10)
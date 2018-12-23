''''''
'''
在我们的进程中
   堆栈区 [栈区（基本数据类型）堆区（对象类型的）]（变量）   常量区（常量）    代码段区（代码） 


'''


'''值传递
传递的不可变的类型

string  tuple  number是不可变的

'''
def fun(num):
    print(id(num))
    num = 10
    print(id(num))
temp = 20
print(id(temp))
fun(temp)  #num=temp=20
print(temp)

#temp并没有变

#值传递不改变实参而改变形参

'''引用传递

传递的可变类型
list dict set是可变的

'''
def fun1(lis):
    lis[0] = 100
li = [1, 2, 3, 4]
fun1(li)
print(li[0])

'''
很有意思的问题来了？？？
'''
a = 10
b = 10
print(id(a))
print(id(b))
#为什么它们的地址是一样的，了解python堆栈的工作原理

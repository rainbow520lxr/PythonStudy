''''''
'''
特殊
1.错误其实是class类，所有的错误继承自BaseException，所以在捕获的时候，它捕获了该类型的错误，还把
子类一网打尽
'''

try:
    print(5/0)
except NameError as e:
    print("NameError")

'''
特殊
跨越多层调用,main调用了fun2, fun2调用了fun1，fun1有错误，这是只要main捕获到了就可以处理
'''

def fun1(num):
    print(1/ num)
def fun2(num):
    fun1(num)
def main():
    fun2(2)
main()

#怎么捕获多层的异常

try:
    main()
except ZeroDivisionError as e:
    print("*****")

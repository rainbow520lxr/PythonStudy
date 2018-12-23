''''''
'''
 概念：不使用def这样的语句定义函数，使用lambda来创建匿名函数

特点：
    1.lambda只是一个表达式，函数体比def简单
    2.lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简答的逻辑
    3.lambda函数有自己的命名空间，且不能访问自由参数列表值外的或全局命名空间的参数
    4.虽然 lambda是一个表达式且看起来只能写一行，与C与C++内联函数不同
    
写python是网络数据请求型处理型不是IO速率行的所以python不适合写桌面应用

格式： lambda 参数1， 参数2， .... ，参数n:expression(这个表达式好比def函数的return的表达式)

        调用：函数名(参数列表)
'''
sum = lambda num1, num2:num1+num2
print(sum(1,2))
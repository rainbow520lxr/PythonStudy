'''
if语句

格式:
if 表达式:
    语句

逻辑：当程序执行到if语句时，首先计算“表达式”的值。
如果“表达式”的值是真，那么执行if下的语句
如果表达式的值为假，if语句继续向下执行


何为真假？
假：0  0.0  ''  None  False
真：除了假都是真

'''
num5 = 10
num6 = 10
if num5 == num6:
    num5 = 100
print("num5 =", num5)

'''
if-else语句

格式：
    if 表达式：
        语句1
    else 表达式
        语句2

逻辑：当程序执行if-else语句时，首先计算”表达式“的值，
如果”表达式“的值是真，则执行语句1。执行完“语句1”跳出整个if-else语句。
如果表达式的值为假，则执行语句2.执行完语句2跳出整个if-else语句

'''

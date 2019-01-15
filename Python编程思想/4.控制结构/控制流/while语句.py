'''
while语句：

格式：

while 表达式：
    语句

逻辑：当程序执行到while语句时，首先计算“表达式”的值，
如果“表达式”的值为假，那么结束整个while语句，
如果表达式的值为真，则执行语句，再执行表达式，并判断真假，同理往上
直到为假跳出循环

'''

'''
计算1+2+3+...+100
'''
sum = 0
num = 1
while num<=100:
    sum += num
    num +=1

print("sum =", sum)

'''
逐个打印字符串中的字符
'''
str = "lxr is a good man"
index = 0
while index < len(str):
    print("str[%d] = %s" % (index, str[index]))
    index +=1


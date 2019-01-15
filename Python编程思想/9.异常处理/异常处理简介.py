''''''
'''
    利用异常python去破解别人的帐号密码

需求：当程序遇到问题时不让程序结束，而越过错误继续向下执行


try......except....else

格式1：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句2
except 错误码 as e:
    语句3
    ...
except 错误码 as e:
    语句n
    
else:               #如果一个错误都没检测到的话就执行这个else
    语句e

作用：用来检测try语句快中的错误，从而让except来捕获错误信息
信息并处理

逻辑：当程序执行到try-except-else执行出现错误时。
 1.如果当try“语句t”执行出现错误，会匹配第一个错误妈，如果匹配上了就执行对应语句
 2.如果当try语句t执行没有错误，没有匹配的异常，错误将会被提交到上一层的try语句。或者到程序的最上层
 3.如果没有错误则执行else
    
注意：else语句可有可无

'''


'''通常怎么用'''

try:
    print (4/0)
except:
    print("程序出现了异常")

#使用expcept带着多种异常,统一去处理
try:
    pass
except (NameError, ZeroDivisionError):
    print("出现了NaameError或者ZeroDivisinError")






























































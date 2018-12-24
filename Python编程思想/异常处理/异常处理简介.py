''''''
'''
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
else:
    语句e

作用：用来检测try语句快中的错误，从而捕捉错误
    
注意：else语句可有可无

'''

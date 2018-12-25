''''''
'''

try......except....finally..

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
    
finally:               #不管怎样都要执行finally
    语句e
'''

try:
    print(1/0)
except ZeroDivisionError as e:
    print("错了")
finally:
    print("*******")
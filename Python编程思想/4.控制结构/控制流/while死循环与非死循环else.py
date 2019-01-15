'''
死循环：表达式永远为真的循环
'''

# while 1:
#     print("lxr is a good man!")

'''
while 表达式：
    语句1
else:
    语句2
    
逻辑：在条件语句（表达式）为False时执行else的"语句2"
'''
a = 1
while a <= 3:
    print("lxr is a good man!")
    a += 1
else:
    print("very good!")


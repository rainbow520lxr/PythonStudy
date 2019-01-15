''''''
'''
不同类型的加法会有不同的解释
'''

class Person(object):
    def __init__(self, num):
        self.num = num
    #运算符重载,重写
    def __add__(self, other):
        return  Person(self.num + other.num)
    def __str__(self):
        return  "num =" + str(self.num)


per1 = Person(12)
per2 = Person(12)

print((per1 + per2))  #把这个加法重新定义等于per1.__add__(per2)
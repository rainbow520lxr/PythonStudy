
#创建一个空类
class Person(object):
    __slots__ = ("name", "age") #限制动态添加的属性

per = Person()

#动态添加属性，这样体现了动态语言的特点（灵活）
per.name = "tom"
print(per.name)

#动态添加方法
def say(self):
    print("你好啊")

from types import MethodType

per.speak = MethodType(say, per)  #给对象添加方法，需要引入一个模块，这个参数是方法，对象


per.speak()

#思考：如果我们想要限制实例的属性怎么办？
#比如，只允许给对象添加name,age,height,weight属性

#解决;定义的时候，定义一个特殊的属性（__slots__),可以限制动态动态添加的属性
'''
    __slots__ = ("name", "age") #限制动态添加的属性
'''
per.speak = "asd"  #这就不能添加

''''''

'''
重写：将函数重新写一遍
__str__():在调用print打印对象时自动调用，是给用户用的，打印该实例的信息
__repr__():是给机器用的，在Python解释器里面敲对象名在回车调用的方法
注意：在没有str时，具有repr,str = repr

'''
class Person(object):

    def __init__(self, name, age, heigtht, weight):
        print(name, age, heigtht, weight)
        #这个self指的是当前创建的对象
        self.name = name
        self.age = age
        self.height = heigtht
        self.weight = weight
    def __str__(self):
        return "这里是stra"

per = Person("lxr", 20, 30, 21)
print(per.name, per.age)
#打印__str__的返回值
print(per)

#当一个对象的属性值很多，都需要打印，重写了__str__,简化代码


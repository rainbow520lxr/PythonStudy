''''''

'''
self代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__ 代表类名

注意;self可以换成其他标识符，但不建议

'''
class Person(object):
    def run(self):
        print("run")

    def eat(self, food):
        print("eat" + food)

    def say(self):
        print("Hell! name is %s, age is %d" % (self.name, self.age))

    def __init__(self, name, age, heigtht, weight):
        print(name, age, heigtht, weight)
        # 这个self指的是当前创建的对象
        self.name = name
        self.age = age
        self.height = heigtht
        self.weight = weight

per1 = Person("lxr", 20, 170, 55)
per1.say()
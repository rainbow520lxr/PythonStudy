''''''
'''
问题：当我们实例化对象时发现，所有实例化对象时，他们的属性值都是一样的和初始行为一致，
怎样使得每个对象实例化时都可以有不同的初始的属性值初始化行为，这不符合现实规律，需要用到构造函数
'''
class Person(object):
    #定义属性(定义变量）
    # name = ""
    # age = 0
    # height = 0
    # weight = 0
    #定义方法（定义函数）
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例（某个对象）
    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)

    def __init__(self, name, age, heigtht, weight):
        print(name, age, heigtht, weight)
        #这个self指的是当前创建的对象
        self.name = name
        self.age = age
        self.height = heigtht
        self.weight = weight
'''
构造函数：__init__() 在使用类创建对象的时候自动调用

对于python有了构造函数，该类的属性则在构造函数中定义

注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数


'''

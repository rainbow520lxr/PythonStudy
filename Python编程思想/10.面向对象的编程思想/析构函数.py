''''''
'''
python会在程序执行完后自动释放对象
析构函数：__del__()  释放对象是自动调用
每个类里面都有一个析构函数，但没操作，但一定会执行


'''
class Person(object):
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
    def __del__(self):
        print("这里是析构函数")  #当释放对象的时候执行

# per = Person("lxr", 10, 10, 10)
#
# del per      #手动释放
#
# while 1:    #可见程序在执行时不会执行析构函数
#     pass

#函数内定义的对象，在函数结束时自动释放
def fun():
    per = Person("lxr", 10, 10, 10)
fun()



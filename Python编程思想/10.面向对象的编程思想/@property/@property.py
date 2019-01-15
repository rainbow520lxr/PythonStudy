''''
简化私有属性的访问操作

可以过滤数据
'''

class Person(object):
    def __init__(self, age):
        # 属性直接对外暴露
        # self.age = age
        # 限制访问
        self.__age = age

    # def getAge(self):
    #     return self.__age
    # def setAge(self, age):
    #     if age < 0:
    #         age = 0
    #     self.__age = age

    #方法名为受限制的变量去掉双下划线
    @property   #限制访问的装饰器
    def age(self):
        return self.__age
    @age.setter  #去掉下划线的.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age

per = Person(12)
#属性直接对外暴露
#不安全，没有数据的过滤
#per.age = -10
#print(per.age)

#使用限制访问，需要自己写set和get方法才能访问
# per.setAge(15)
# print(per.getAge())

#使用点的方式访问被限制访问的变量
per.age = 100
print(per.age)

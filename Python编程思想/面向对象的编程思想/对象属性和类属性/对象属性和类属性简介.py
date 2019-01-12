'''

类属性不要和对象属性同名，否则对象属性会对类属性覆盖

对象属性由对象调用，类属性由类名来调用



'''

class Person(object):
    #这里的属性实际上输入类属性（用类名来调用的属性）
    name = "person"
    def __init__(self, name):
        pass
        # self.name = name

per = Person("tom")
per.name = "aaa"  #在这里添加了一个对象属性
#对象属性高于类属性
print(per.name)
#动态添加属性
per1 = Person("jerry")
per1.age = 12
print(per1.age)

print(Person.name)
#删除对象中的name属性
del per.name

#删除同名的类属性和对象属性则，会出现类属性表达


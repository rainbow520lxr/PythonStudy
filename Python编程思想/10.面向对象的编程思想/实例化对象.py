class Person(object):
    #定义属性(定义变量）
    name = ""
    age = 0
    height = 0
    weight = 0
    #定义方法（定义函数）
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例（某个对象）
    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)

'''
实例化对象
格式： 对象名 = 类名（参数列表）
注意：没有参数，小括号也不能省略

'''
#实例化一个对象,分配空间
per1 = Person()
print(per1)
print(type(per1))

per2 = Person()
print(per2)
print(type(per2))
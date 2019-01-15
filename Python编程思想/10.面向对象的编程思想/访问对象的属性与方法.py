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
访问属性
格式：对象名.属性名
赋值：对象名 = 值
'''

'''
访问方法：
格式：对象名.方法名（参数列表） #从self后面第一参数开始才为参数列表

'''
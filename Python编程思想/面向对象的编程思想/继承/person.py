class Person(object):
    def __init__(self, name, sex, money):
        self.name = name
        self.sex = sex
        self.__money = money
    def run(self):
        print("我会跑")
    def eat(self, food):
        print("我要吃%s" % food)


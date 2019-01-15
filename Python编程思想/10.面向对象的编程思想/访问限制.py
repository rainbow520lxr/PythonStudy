class Person(object):

    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)
    #通过内部方法，去修改私有属性
    def setMoney(self, money):
        #数据过滤
        if money<0:
            print("请输入正确的money")
        self.__money = money
    def getMoney(self):
        return self.__money
    def __init__(self, name, age, heigtht, weight, money):
        print(name, age, heigtht, weight)
        #这个self指的是当前创建的对象
        self.name = name
        self.__age__ = age
        self._height = heigtht
        self.weight = weight
        self.__money = money

per = Person("lxr", 10, 20, 30)
#很容易修改对象内部属性值
per.age = 10

#如果要让内部属性不被外部直接访问,就要在属性前加两个下划线,那么属性就变成了私有属性,内部可以是哦那个

#print(per.__money)
per.__money = 10  #这里虽然看似改值实际上是该对象动态添加属性

#不能直接访问per.__money是因为Python解释器把__money编程了_Person__money这个才是最终的私有属性,仍然可以用
#_Person__money 去访问，但是强烈建议不要这么干，不同的解释器可能存在解释的变量名不一致

#在Python中__XXX__  属于特殊变量，可以直接访问
print(per.__age__)

#在Python中，_XXX变量，这样的实例变量外部是可以访问的，但是，按照约定的规则，当我们看到这样的变量时
#意思是"虽然我可以被访问，但是请把我视为私有变量，不要直接访问我
print(per._height)





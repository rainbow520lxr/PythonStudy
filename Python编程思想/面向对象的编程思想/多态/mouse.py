from animal import Animal
class Mouse(Animal):
    def __init__(self, name):
        # self.name = name
        super(Mouse, self).__init__(name)
    # def eat(self):
    #     print(self.name+"我能吃")

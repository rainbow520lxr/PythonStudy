from father import Father
from mother import Mother

class Child(Mother, Father):    #这里可以写多个父类名
    def __init__(self, money, faceValue):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)


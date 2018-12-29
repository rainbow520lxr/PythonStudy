from person import Person

class Student(Person):
    def __init__(self, name, sex, money, id):
        #调用父类中的__init__
        super(Student, self).__init__(name, sex, money)
        #子类独有的一些属性
        self.id = id


from student import Student

stu = Student("tom", "男", 100, 100)
stu.eat("水果")
print(stu.id)
#父类的私有属性无法继承过来，因此父类一般都定义公有的属性
#可以用get和set方法来进行访问这个父类的私有属性
print(stu.__money)
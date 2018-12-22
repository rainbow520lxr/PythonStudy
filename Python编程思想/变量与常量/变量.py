#程序执行的过程：自上而下顺序执行（面向过程）


age = 0
age = 18

#del age
#删除变量，释放空间


print("age = ", age)
#变量在使用之前必须先定义

print(type(age))
#查看变量的类型
print(id(age))
#查看变量的地址


num1 = input("请输入一个数字：")
num2 = input("请再输入一个数字：")

print("num1 + num2 = ",num1+num2)



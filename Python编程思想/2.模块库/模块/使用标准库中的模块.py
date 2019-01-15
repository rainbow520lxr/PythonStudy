''''''
'''
引入系统模块
'''
import sys


print(sys.argv)
#获取命令行的参数的列表
for i in sys.argv:
    print(i)
name = sys.argv[0]
age = sys.argv[1]
print(name, age)




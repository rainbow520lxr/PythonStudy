''''''
import itertools
import time

'''
迭代工具 排列组合工具
'''
mylist = list(itertools.product("0123456789" ,repeat = 3)) #密码
mylist1 = list(itertools.combinations("0123456789" ,3))  #排列组合
print(len(mylist))
print(mylist)
print(mylist1)

password = ("".join(x) for x in itertools.product("0123456789" ,repeat = 3))

while True:
    try:
        time.sleep(0.5)
        str = next(password)
        print(str)
    except StopIteration:
        break


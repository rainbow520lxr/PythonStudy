from collections import  Iterable
from collections import  Iterator

''''''
'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象
（iterable)。可以用isinstance()去判断一个对象是否是iterable对象

可以直接作用于for的数据类型一般分两种
1.集合数据类型，如list\tuple\dict\set\string
2.是generator,包括生成器和带yield的generator function

'''

#判断是否为可迭代对象
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance(1, Iterable))
print(isinstance((x for x in range(10)), Iterable))
#判断是否为迭代器
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance(1, Iterator))
print(isinstance((x for x in range(10)), Iterator))

'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
，直到最后跑出一个StopItration错误，表示无法继续返回下一个值


可以被next()函数调用并不断返回下一个值的对象称为迭代器
(Iterator对象)


可以使用instance()函数判断一个对象是否是Iterator对象
'''

'''迭代器使用
'''
l = (x for x in range(5))#生成一个迭代器
print(l)
print(next(l))
print(next(l))
print(next(l))
# print(next(l))


'''转成一个Iterator对象
'''
a = iter([1, 2, 3, 4, 5])
print(next(a))
print(next(a))

print(isinstance(iter(()), Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(""), Iterator))

'''在终端输入能换行输入, iter(迭代函数，迭代对象中的终止迭代项)
endstr = "end"
str = ""
for line in iter(input, endstr):
    str += line + "\n"
print(str)
'''

for x in iter([1, 2, 3, 4, 5, 6]):
    print(x)


'''迭代器的生成作用
'''
l = [x for x in range(5)]
print(l)
l1 = {x for x in range(5)}
print(l1)

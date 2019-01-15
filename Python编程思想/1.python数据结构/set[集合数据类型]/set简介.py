''''''
'''
set:类似dict,是一组key的集合,而key是内部不可变类型，因此不能添加列表和字典，而可以添加元组，不存储value

本质：无序和无重复元素的集合

特点：集合没有索引

格式：set = {1, 2, 3, 4, 5}

常用功能：在于对list和tuple去重

'''
'''创建
创建set需要一个list或者tuple或者dict作为输入集合
'''
sl = set([1, 2, 3, 3, 4])#重复的元素自动过滤
print(sl)
s2 = set((1, 2, 3, 3, 4))
print(s2)
s3 = set({"lxr":"asdd", "lxy":"asdd"})
print(s3)

'''添加
'''
s4 = set([1, 2, 3, 4, 5])
s4.add(6)
print(s4)
s4.add(1)
print(s4)

'''s5.update(),插入整个list、tuple、字符串，打碎插入,将其分为一个个字符插入
'''
s5 = set([1, 2, 3, 4, 5])
s5.update([6, 7, 8])
print(s5)
s5.update((9, 10))
s5.update(("sunck"))
print(s5)

'''删除，不能根据下标删除,只能按照值来删除
'''
s5.remove(3)
print(s5)

'''删除
'''
s7 = set([1, 2, 3, 5])
for i in s7:
    print(i)

'''枚举遍历
'''
for index, data in enumerate(s7):
    print(index, data)



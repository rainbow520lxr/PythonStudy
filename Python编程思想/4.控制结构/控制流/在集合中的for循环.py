'''
for语句
格式：
for 变量名 in 集合：
    语句

逻辑：按顺序取"集合"中的每个匀速赋值给“变量”,在去执行
语句，如此循环往复，直至取完“集合”中的元素截至
'''

'''列表中'''
for i in [1, 2, 3, 4]:
    print(i)

'''range()函数

功能：列表生成器
range(100)
range([start,] end[, step])
生成0到99
'''
for x in range(10):
    print(x)

for y in range(2, 20, 2):
    print(y)

#同时遍历下标和元素
for index, m in enumerate([1, 2, 3, 4, 5]):   #index,m =下标， 元素 enumerate()枚举器
    print(index, m)

#for能更清晰







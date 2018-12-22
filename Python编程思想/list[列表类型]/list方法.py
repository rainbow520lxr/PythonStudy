''''''
'''列表方法
append(6) 在列表中末尾添加新的元素
list = [1,2,3,4,5,6]
list.apped(6)

extend([1,2,3])在末尾追加多个元素
list = [1,2,3,4,5,6]
list.extend([3,4,8])


'''
#追加单个元素
list = [1,2,3,4,5,6]
list.append(7)
print(list)

'''
在列表中插入一个值,insert(index, value)在index小标的后面插入一个值，原数据顺延
'''
list = [1, 2, 3, 4, 6]
list.insert(2, 100)
print(list)

list.insert(2, [200, 300])
print(list)

'''
list列表中删除
1.按下标来删除
list.pop()默认是pop(x=list(-1))-1默认代表列表最后一个下标
list.pop(2)
删除后并返回删除后的列表
2.按列表中的列表项值来删除
remove(value) 移除列表中的某个元素第一个匹配结果
list = [1, 2, 3, 4, 5, 4, 6]
list.remove(4)
3.清除列表中所有的数据
list.clear(list)
'''

'''
list列表值的查找
list = [1, 2, 3, 4, 5]
value1 = list.index(1)
value2 = list.index(1, 2, 3)
print(value1, value2)
'''
list = [1, 2, 3, 4, 5]
# 查找下标
value1 = list.index(1)
# 这里是在下标1到5中查找值为3的下标
value2 = list.index(3, 1, 5)
print(value1)
print(value2)

'''
获取列表中的最大值,最小值
'''
list = [1, 2, 3, 4, 5]
print(max(list))
print(min(list))

'''
查看元素在列表中出现的次数
'''
list = [1, 2, 3, 4, 5, 3]
print(list.count(3))

'''
列表顺序倒序
list = [1, 2, 3, 4, 5]
'''
list = [1, 2, 3, 4, 5]
list.reverse()
print(list)

'''
排序 升序
'''
list.sort()
print(list)

'''
拷贝
'''
#浅拷贝
list1 = list
list[1] = 3
print(list[1])
print(list1[1])
print(id(list[1]))
print(id(list1[1]))

#深拷贝
list1 = list.copy()
list[1] = 1
print(list[1])
print(list1[1])

'''
将元组转成列表
'''



















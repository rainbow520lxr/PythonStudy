'''
元组的方法
'''


#len()  返回元组中元素的个数
t = (1, 2, 3, 4, 5)
print(len(t))

#将max() 返回元组中的最大值最小值
print(max((1, 2, 3, 5, 6)))
print(min((1, 2, 3, 5, 6)))

#将列表转成元组
list = [1, 2, 3]
t = tuple(list)
print(t)


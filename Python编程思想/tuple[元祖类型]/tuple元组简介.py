
'''

思考：为什么要有了列表还要有元组？
元组的数据不可变性，给数据带了安全，一般我们在搞数据存储时用元组好点
但tuple的方法和操作很少

'''



#创建空的元祖
tuple = ()

print(tuple)

#创建带有元素的元祖
#元组中的元素的类型可以不同

tuple = (1, 2, 3, "good", True)
print(tuple)

#定义一个只有一个元素的元组
tuple = (1, )
tuple1 = (1)
print(tuple)
print(type(tuple))

print(tuple1)
print(type(tuple1))
#因此可以看出单元素的元组后面要加,号；不然是数字1

list = [1]
print(list)
print(type(list))

#元组的元素的访问
# 格式：元组名[下标]
tuple = (1, 2, 3, 4)
print(tuple[2])
print(tuple[-1]) #获取最后一个元素的值，元组-6才越界负数的下标代表从后往前取值

tuple[1] = 0 #元组的元素一旦初始化就不能变

#元组的删除，只能将元组整个删除
tuple = (1, 2, 3)
del tuple



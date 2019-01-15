'''
控制流表达式可以输出值
'''

'''
for循环表达式
'''
X = [1, 2, 3, 4, 5]
Y = [x*3 for x in X]
print(Y)
print(id(X))
print(id(Y))

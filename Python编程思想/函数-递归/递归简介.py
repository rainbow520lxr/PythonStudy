''''''
'''
递归调用：一个函数，调用了自身，称为递归调用
递归函数：一个会调用自身的函数称为递归函数

凡是循环能干的事，递归都能干
'''

'''
方式：

1.写出临界条件
2.找这一次和上一次的关系
3.假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果

'''
#输入一个数（大于等于1），求1+2+3+...+n的和
# def sum(n):
#     sum = 0
#     for x in range(1, n + 1)
#         sum += x
#     return sum
# res = sum(5)
# print("res =", res)


def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1)+n
print("sum =", sum(10))


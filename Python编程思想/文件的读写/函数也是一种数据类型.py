def sum(a, b):
    return a + b

#函数也是一种数据类型f也指向sum的栈顶指针
f = sum
#不加小括号不执行
a = f(1, 2)
res = sum(1, 2)
print(res)
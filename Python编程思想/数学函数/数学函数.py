import math #封装的数学库导入库，封装的功能模块函数
import random#随机数库

#存在系统库，和导入库
#Python的系统库不用在前面加库名，而导入的库要在前面加库名
#数学功能

a1 = -10
#取正数
a2 = abs(a1)

print(a2)

#比较两数的大小
a3 = 6
a4 = 9
print((a3>a4)-(a3<a4))

#返回函数的最小值
print(max(1, 2, 3, 4, 5))

#求x的y次方 2^5
print(pow(2, 5))

#round
print(round(3.456))#四舍五入
print(round(3.456, 1))#四舍五入,保留一位
print(round(3.456, 2))#四舍五入，包留两位

#使用导入库
print(math.ceil(18.6))
print(math.modf(22.3))#返回整数部分和小数部分

#随机数的生成
print(random.choice([1, 3, 5, 7, 9]))#从序列中随机选取一个数
print(random.choice([1, 3, 5, 7, 9, "aa"]))#从序列中随机选取一个数,也可以在序列中加入字符串
print(random.choice(range(5)))#range(5) == [0, 1, 2, 3, 4]
print(random.choice("sunck"))#"sunck" == ["s", "u", "n", "c", "k"]将其看成一个序列

#产生一个1~100之间的随机数
r1 = random.choice(range(10)) + 1#生成一个1到10的数
print(r1)

#random.randrange([start,] stop[,step])中括号的意思是可以不用的参数
#start——制定范围的开始值，包含在范围内
#stop——制定范围的结束，不包含在范围内
#step——指定的递增基数，默认是1
print(random.randrange(1,100,2))
#从0-99选一个随机数
print(random.randrange(100))
#随机生产【0,1）之间的数（浮点数）
print(random.random())

list = [1, 2, 3, 4, 5]
#将序列的所有元素随机排序
random.shuffle(list)
print(list)

#随机生产一个实数，他在【3,9】中的特征不一样的是两端都包含
print(random.uniform(3, 9))




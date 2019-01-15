import time
#以第一次为基数
y = time.clock()
print(y)
sum = 0
for i in range(10000):
    sum += i
print("%d" % time.clock())


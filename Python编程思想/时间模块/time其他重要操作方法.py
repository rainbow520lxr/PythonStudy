import time

# 延迟一个时间，整型或者浮点型
# time.sleep(4) #让当前进程或者线程睡眠多少秒

# 返回当前程序的cpu执行时间
# Unix形同始终返回全部的运行时间
# windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数
# 打印四种
y1 = time.clock()
print(y1)
time.sleep(2)
y2 = time.clock()
print(y2)

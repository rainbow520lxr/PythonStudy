import datetime

dt = datetime.datetime.now()
dt1 = datetime.datetime(1999, 10, 1, 10, 28, 25, 123456)
dt2 = dt - dt1
print(dt2)
print(type(dt2))
#打印间隔天数
print(dt2.days)
#打印除间隔天数的秒数
print(dt2.seconds)

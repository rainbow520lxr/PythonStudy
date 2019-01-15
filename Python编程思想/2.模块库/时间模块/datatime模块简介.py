''''''
import datetime
'''
datatime比time高级了不少，可以理解为datatime基于time进行了封装，提供了各种使用的函数，datatime模块的几口更直观，
更容易调用


模块中的类：
datatime  同时有时间和日期
timedelta  主要用于计算时间的跨度
tzinfo  时区相关
time  只关注时间
data 只关注时期

'''

#获取当前时间
dt1 = datetime.datetime.now()
print(dt1)
print(type(dt1))

#获取指定时间
dt2 = datetime.datetime(1999, 10, 1, 10, 28, 25, 123456)
print(dt2)

#将时间转为字符串
s = dt1.strftime("%Y-%m-%d %X")
print(s)
print(type(s))

#将格式化字符串转为datatime对象
#注意：转换的格式要与字符串一致
dt4 = datetime.datetime.strptime(s, "%Y-%m-%d %X")
print(dt4)






import time

#返回当前时间的时间戳，浮点数形式，不需要参数
c = time.time()
print(c)

#将时间戳作为UTC时间元组
t = time.gmtime(c)
print(t)

#将时间戳转为本地时间元组
m = time.localtime(c)
print(m)

#将本地时间元组转成时间戳
d = time.mktime(m)
print(d)

#将时间元组转成字符串
s = time.asctime(m)
print(s)

#将时间戳转为字符串  time.asctime(time.localtime(tie.time()))
p = time.ctime(c)
print(p)

#将时间元组转成给定格式的字符串，参数2为时间元组，如果没有参数2，默认转当前时间
q = time.strftime("%Y-%m-%d %X", m)
print(q)
print(type(q))

#将时间字符串转为时间元组
w = time.strptime(q, "%Y-%m-%d %X")
print(w)
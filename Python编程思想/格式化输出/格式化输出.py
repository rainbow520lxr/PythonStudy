#格式化输出
print("sunc is a good man")
num = 10
print("num =", num)
str19 = "sunck is a nice man!"
print("num =", num, "str19 =", str19)
print("num = %d, str19 = %s" %(num, str19))

f = 10.126
print("num = %d, str19 = %s, f = %.3f" % (num, str19, f))# .3精确到小数点后3位，会四舍五入

# 转义字符换行字符，将一些字符换成有特殊含义的字符
'''
\n 换行符
\\n  将转义字符进行转义表示\n
\\   表示\
\'   表示'
'''


print("num = %d\n str19 = %s\n f = %.3f" % (num, str19, f))# .3精确到小数点后3位，会四舍五入

#对于字符串中有”“’‘
print("tom is a \'good\' man")
print("tom is a \"good\" man")
print("tom is a 'good' man")

# 字符串内有很多换行，用\n写在一行不好阅读,python中独有的
print('''
good
nice
handsome
''')

#四个空格\t
print("sunck\tgood")

print("\\\t\\")
#如果字符串中有好多字符串都需要转义， 就需要加入好多\， 为了简化，
# python允许用r表示内部的字符串默认不转义
print(r"\\\t\\")
'''
例子windows路径
'''
# print("c:\users\xlg\desktop") 报错
print(r"c:\users\xlg\desktop")
print("c:\\users\\xlg\\desktop")
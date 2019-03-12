import re

#pip 包管理工具

'''
re.match函数

原型：match(pattern, string, flags=0)
参数：
patter 匹配的正则表达式
String 要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式，值如下
re.I  忽略大小写
re.L  做本地户识别
de.M  多行匹配，影响-和$
de.S  是匹配包括换行符在内的所有字符
re.U  根据Unicode字符集解析字符，影响\w \W \b \B
re.X  使我们以更灵活的格式理解正则表达式

功能：尝试从字符串的起始位置匹配一个模式，如果不是起始位置
匹配成功过的话，返回None

'''


print(re.match("www", "www.baidu.com"))
print(re.match("wwW", "www.baidu.com", flags=re.I))
print(re.match("www", "www.baidu.com").span())  #打印位置
#扫描整个字符串，返回从起始位置成功的匹配

'''
re.search函数  
原型：search(pattern, string, flags=0)
参数：
patter 匹配的正则表达式
String 要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回第一个成功的匹配

'''
print(re.search("sunck", "good man is sunck!sunck is nice"))


'''
re.findall函数
原型：search(pattern, string, flags=0)
参数：
patter 匹配的正则表达式
String 要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：扫描整个字符串，并返回结果列表

'''
print(re.findall("sunck", "good man is sunck!Sunck is nice", flags=re.I))



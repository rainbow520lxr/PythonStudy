import re

'''字符串切割
'''

str1 = "sunck#######is a good man"

print(re.split(r" +", str1))


'''
re.finditer函数
原型： finditer(pattern, string, flag=0)
参数：

patter: 匹配的正则表达式
string: 要匹配的字符串
flags: 标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
使用迭代器可以减小你返回需要使用的内存
'''
str2 = "sunck is a good man! sunck is a nice man! sunck is a handsome man"
d = re.finditer(r"(sunck)", str2)
# while True:
#     try:
#         a = next(d)
#         print(d)
#     except StopAsyncIteration as e:
#         break


'''
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, rep1, string, count=0, flags=0)
pattern: 正则表达式（规则）
repl:指定的用来替换的字符串
string:目标字符串
count:最多替换次数
功能：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。可以指定替换的次数，如果不指定，替换所有的匹配字符串

区别： 前者返回一个被替换的字符串，后者返回一个元组，第一个元素被替换的字符串，第二个元素表示被替换的次数
'''
str3 = "sunck is a good good good man"
# print(re.sub(r"(good)", "nice", str3))
# print(type(re.sub(r"(good)", "nice", str3)))
print(re.subn(r"(good)", "nice", str3))
print(type(re.subn(r"(good)", "nice", str3)))






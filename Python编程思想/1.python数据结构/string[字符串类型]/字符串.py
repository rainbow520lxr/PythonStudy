'''
什么是字符串？
字符串是以单引号或双引号括起来的任意文本
'abc'
"def"
'''

#创建字符串
str1 = "sunck is a good man!"


'''
字符串运算
'''

#字符串连接
str1 = "sunck is a"
str2 = "a good man"
str = str1 + str2
print("str =", str)

#输出重复的字符串
str3 = "good"
str4 = str3*3#拼接
print("str3 =",str4)


#访问字符穿中的某一个字符
#通过索引下标查找字符，索引从0开始
str5 = "sunck is a good man"
print(str5[0])
'''
str5[0] = "a"
print(str5)报错，字符串不能更改单独的字符 

'''

#截取字符串的一部分
str13 = "sunck is a good man!"
str15 = str13[6:14]
# 从给定下标开始截取到给定下标之前，python一般都是左臂右开
print("str15 =", str15)
# 从头截取到给定下标之前
str17 = str13[:15]
print("str17 =", str17)
# 从给定的下标到末尾
str18 = str13[4:]
print("str18 =", str18)

# 是否在子字符串在原字符串中

print("good" in str13)
print("good1" in str13)

print(~5)
# 00000101补码        反算
# 11111010反码
# 10000110原码

#eval(str)
#功能：将字符串str当成有效的表达式来求值并返回计算结果
num1 = eval("123")
print(num1)
print("+123")
print("-123")
print("12+3")
print("12-3")
print(eval("123"))

#len(str)
#返回字符串的长度，字符的个数
print(len("sunck is a good man凯"))

#str.lower(self)转换字符串中大写字母位小写字母
str20 = "SUNCK is a good Man!"
print(str20.lower())
print("str20 =%s" % str20)

#str.upper(self)转换字符串为大写字母
print(str20.upper())

#capitalize()  首字母大写，其他小写
print(str20.capitalize())

#tile()每个单词的首字母大写
print(str20.title())

#center(with, fillchar)在with的宽度的字符串空间中，self放在中间，其他填充a
print(str20.center(30, 'a'))

#ljust(with[,fillchar])返回一个指定宽度的左对齐，fillchar位填充字符，默认空格填充
print(str20.ljust(40,"%"))
#ljust(with[,fillchar])返回一个指定宽度的右对齐，fillchar位填充字符，默认空格填充
print(str20.rjust(40,"%"))

#zfill(with)返回一个长度为width的字符串，原字符串右对去，前面补0
print(str20.zfill(40))

#count(str[,start][,end])从指定的一个范围中，默认从头到尾，去查看在self字符串中出现的次数
print(str20.count("veryadqdasdasda",1,5))

#find(str[,start][,end]), rfind(str[,start][,end])#从右向左
# 从左向右检测str字符串是否包含在字符中，可以指定范围，默认从头到尾，得到的是第一次出现的开始下标，没有返回-1
str = "nihao"
print(str.find("ni"))
print(str.find("hao"))
print(str.find("hao", 0, 5))

#index(str, start=0, end=len(str)
#根find（）一样，只不过如果str不存在的时候回报一个异常
str = "kaige is a very very nice man"
print(str.index("very"))

print(str.rindex("very"))

#str.lstrip截掉字符串左侧指定的字符，默认空格
str = "   lxr is good man    "
print(str.lstrip())
print(str.rstrip(), "*")
#str.strip()截取掉参数字符
str = "**********nihao*************"
print(str.strip("*"))






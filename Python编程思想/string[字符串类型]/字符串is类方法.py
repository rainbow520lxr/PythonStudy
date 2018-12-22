#isalpha()
#如果字符串中至少有一个字符且所有的字符都是字母返回True,否
str = "asASds123"
print(str.isalpha())

#isalnum
#如果字符串中至少有一个字符且所有的字符都是字母或数字返回True,否
print(str.isalnum())

#isupper()
#如果字符串中至少有一个字符且所有的字符都是大写的英文字母返回True,否
print(str.isupper())

#islower()
#如果字符串中至少有一个字符且所有的字符都是小写的英文字母返回True,否
print(str.islower())

#istitle()
#如果字符串是标题化的返回True，否则返回False  标题化是单词的首字母大写的
print("Sunk".istitle())

#isdigit()
#如果字符串中只包含数字返回True，否则False
print("123".isdigit())

#isnumeric()
#如果字符串中只包含数字字符返回True，否则False
print("123".isnumeric())

#isdecimal()
#如果字符串中只包含十进制数字字符返回True，否则False
print("123".isdecimal)


#isspace()
#如果字符串中只包含空格返回True，否则False
print("\t".isspace())
print("\n".isspace())

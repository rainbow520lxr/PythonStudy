import re


print("-------------------匹配单个字符和数字---------)")

'''
匹配单个的元字符

.  匹配除换行符以外的任意字符
[0123456789]  []是字符集合，表示匹配方括号中所包含的任意一个字符
[sunck]       匹配's', 'u', 'c', 'n', 'k'任意一个字符
[a-z]         匹配任意小写字母
[A-Z]         匹配任意大写字母
[0-9]         匹配任意数字，类似[0123456789]
[0-9a-zA-Z]   匹配任意的数字和字母
[0-9a-zA-Z_]  匹配任意的数字和字母和下划线
[^sunck]      匹配除了sunck这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
[^0-9]        匹配所有的非数字字符
\d            匹配数字，效果同[0-9]
\D            匹配非数字字符，效果同[^0-9]
\w            匹配数字，字母和下划线，效果同[0-9a-zA-Z_]
\W            匹配数字，字母和下划线，效果同[^0-9a-zA-Z_]
\s            匹配任意的空白符（空格，换行，回车，换页，制表），效果同[ \f\n\r\t]
\S            匹配任意的非空白符（空格，换行，回车，换页，制表），效果同[^ \f\n\r\t]
'''

print("-------------------锚字符（边界字符）---------)")
'''
^    行首匹配，和在[]里的^不是一个意思 ， 能匹配的每一行的行首
$    行尾匹配
\A   匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头，即使在re.M模式下页不会匹配它行的行首
\Z   匹配字符串结束，它和$的区别是，\Z只匹配整个字符串的结束，即使在re.M模式下页不会匹配它行的行首
\b   匹配一个单词的边界，也就是值单词和空格间的位置 不能是单词内部
     '
\B   匹配非单词边界
'''
print(re.search("^sunck", "sunck is a good man\nsunck is a good man"))
print(re.search("\Asunck", "sunck is a good man"))
print(re.search("man$", "sunck is a good man"))
print(re.search(r"er\b", "never "))
print(re.search(r"er\b", "never nihao"))

print("-------------匹配多个字符----------------)")
'''
在前面加r表示原生字符字符串内的\就不会被转义
说明：下方的x、y、z均为假设的普通字符，不是正则表达式的元字符
（xyz)  匹配小括号内的xyz(作为一个整体去匹配）
x?      匹配0个或者1个x
x*      匹配0个或者任意多个x(.*表示匹配0个或者任意多个字符（换行符除外）

x+      匹配至少一个x
x{n}    匹配确定的n个x(n是一个非负整数）
x{n,}   匹配至少n个x
x{n,m}  匹配至少n个最多m个x.注意：n<=m
x|y     |表示或，匹配的是x或y

'''
print(re.findall(r"a?", "aaa"))  #非贪婪匹配
print(re.findall(r"a*", "aaaasddaddd"))  #贪婪匹配
print(re.findall(r".*", "aaaasd"))
print(re.findall(r"a+", "aaaasda"))#贪婪匹配（至少一个）尽可能多的匹配
print(re.findall(r"a{3}", "aaa2aaasd"))
print(re.findall(r"a{2,}", "aa2aaaa2aaasd"))
print(re.findall(r"((s|S)unck)", "sunck--Sunck"))

#需求，提取sunck....man,
str = "sunck is a good man!sunck is a nice man!sunck is a good man!"

print(re.findall(r"^sunck.*man$", str))

print("- - - - - - - - - - - - - - - - 特殊 - - - - - - - - - - - - - - - - - ")
'''
*?  +?  x? 最小匹配 通常都是尽可能多的匹配，可以使用这种解贪婪匹配

(? : x)   类似（xyz)，但不表示一个组
'''
print(re.findall(r"^sunck.*?man$", str))
#注释： /* part1 */    /*   part2    */

print(re.findall((r"//*.*/*/", r"/* part1 */    /*    part2    */")))




'''
字符串的分割,将字符串分割后形成列表
split(str="", num)
以str为分隔符截取字符串，指出num，则仅截取num个字符串
'''
#从下面的字符串中检测出有多少个单词
str = "sunk***is****a*******good*man"
list = str.split("*")
print(list)
c = 0
for s in list:
    if len(s) >0:
        c += 1
print(c)

'''
按行切割
splitlines()  按照('/r' , '/r/n' , '/n')分隔，返回
keepends == True 会保留换行符，一般默认false
'''
str = '''lxr
lxr
lxr
'''
print(str.splitlines(True))

'''
join() 以指定的字符串分隔符，将seq中的所有元素组合成

list

'''
list = ['lxr', 'lxr', 'lxr']
str = "nihao".join(list)
#将nihao字符串加入到列表间隔再组合成字符串
print(str)

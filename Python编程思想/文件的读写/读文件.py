''''''

'''
读文件
过程：
    1.打开文件
    open(path, flag[, encoding][, errors])
    path:要打开文件的路径
    flag:打开方式
    r:以只读的方式打开文件，文件的描述符放在文件的开头
    rb:以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
    r+:打开一个文件用于读写，文件的描述符放在文件的开头
    w:打开一个文件只能用于写入，如果该文件已经存在会覆盖，如果不存在则创建新文件
    wb:打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，如果不存在则创建新文件
    w+:打开一个文件用于读写
    a:打开一个文件用于追加，如果文件存在，文件描述符会放到文件末尾
    a+:
    encoding:编码方式
    errors:错误处理
    
'''

#ignore 忽略错误
path = r"C:\Users\Administrator\Desktop\a.txt"
#打开文件
f = open(path, "r", encoding="utf-8", errors = "ignore")

'''
读文件
'''
#1.读文件全部内容,适合读文件比较小的 *
# str = f.read()
# print(str)

#2.读文件的方式,读取指定字符数
str = f.read(10)


#3.读取整行，包括"\n"字符  *
str = f.readline()
print(str)

#4.读取一行的指定字符数（一般不这么用）
str = f.readline(10)

#5.读取所有行并返回列表  *
list = f.readlines()
print (list)

#6.若给定的数字大于0，返回实际size字节的行数
list = f.readlines()

print ("**************")
#修改描述符的位置
f.seek(o)


'''
关闭文件

'''
f.close()
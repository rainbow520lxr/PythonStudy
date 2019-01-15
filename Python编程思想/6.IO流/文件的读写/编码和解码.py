''''''
'''

编码和解码

对于网络文件传输是以二进制的形式进行的传输的
'''


'''编码'''
pat = "a.txt"

with open(path, "wb") as f2:                 #然而对于打开文件的参数编码是指以怎样的编码格式去打开它而与下方的编码解码无关，但在读取时如果不一致的话设置忽略参数，依旧读取文件但可能乱码
    str = "lxr is a good man"
    fs.write(str.encode("utf-8"))   #如果上面定义了wb形式的写入文件，成二进制文件

'''解码'''
with open(path, "rb") as f2:
    data =f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8") #这里要进行相同的解码
    print(newData)
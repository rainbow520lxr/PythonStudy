path = "a.txt"
f = open(path, "w") #这个是将文本重写

f = open(path, "a")#追加的方式写文本
while 1:
    f.write("lxr is a good man!")
    #等缓冲区满了自动刷新
    time.sleep(0.01)

f.close
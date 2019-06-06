import os


path = r"C:\Users\lxr\Desktop\demo.txt"
log = r"C:\Users\lxr\Desktop\error.txt"
rpath = r"C:\Users\lxr\Desktop\res.txt"
li = []
error1 = []
error2 = []
error3 = []
res = {}

def preprocess(line):
    lenth = len(line) - 4
    new_line = line[lenth:]
    if(len(line) != 12):
        error1.append(line)
    elif(line[:8] != '20175124'):
        error2.append(line)
    return new_line


def write2file(list):
    f = open(log, 'w')
    for i in range(0, len(list)):
        f.write("第"+str(i+1)+"种如下:\n")
        f.flush()
        for item in list[i]:
            f.write(item+"\n")
            f.flush()
    f.close()


def find(list):
    times = 0;
    for i in range(1, 2501):
        for item in list:
            if(i == item):
                times += 1
        if(times in res.keys()):
            res[times].append(i)
        else:
            res[times] = []
            res[times].append(i)
        times = 0




def main():
    f = open(path, "r")
    line = f.readline()
    while line:
        line = line.rstrip('\n')
        line = line.rstrip(' ')
        print(line)
        if(line != ''):
            line = preprocess(line)
            num = int(line)-2400
            if(num > 2500):
                error3.append("20175124"+str(num+2400))
            li.append(num)
        line = f.readline()
    f.close()
    li.sort()
    print(li)
    print("编码总数:"+str(len(li)))
    print("error1: %s" % error1)
    print("error2: %s" % error2)
    print("error3: %s"% error3)
    error = [error1, error2, error3]
    write2file(error)
    find(li)
    print(res)
    f = open(rpath, 'w')
    f.write("搜寻结果完毕！\n——————————————————hello python———————————————————————\n")
    f.flush()
    for k,v in res.items():
        if(k != 1):
            f.write("出现"+str(k)+"次的编号如下：\n")
            f.flush()
            f.write("数量: " + str(len(v)) + "\n")
            f.flush()
            for item in v:
                n = "20175124"+str(item+2400)
                f.write(">>>"+n+"\n")
                f.flush()
    # f.write("——————————————————处理前的总体排序结果—————————————————————————\n")
    # f.flush()
    # f.write("\n\n\n——————————————————处理后的总体排序结果—————————————————————————\n")
    # f.flush()
    # # for i in range(0, len(li)):
    # #     for i % 5
    # #     n = "20175124" + str(li[i] + 2400)
    # #     f.write(">>>" + str(n) + "\n")



    f.close()


if __name__ == '__main__':
    main()

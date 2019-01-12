'''
实现字母的排列组合
26个字母任意抽取三个，需要每个的排列

'''
import pickle  #数据持久性模块
alpha = ["a", "b", "c",
         "d", "e", "f",
         "g", "h", "i",
         "j", "k", "l",
         "m", "n", "o",
         "p", "q", "r",
         "s", "t", "u",
         "v", "w", "x",
         "y", "z"]

for i in range(26):
    alpha[i] = alpha[i].upper()

dict = {}
count = 0



#组合
for a in range(0,26):
    for b in range(a+1, 26):
        for c in range(b+1, 26):
            #排列
            count += 1
            abc=alpha[a] + alpha[b] + alpha[c]
            acb=alpha[a] + alpha[c] + alpha[b]
            bac=alpha[b] + alpha[a] + alpha[c]
            bca= alpha[b] + alpha[c] + alpha[a]
            cab=alpha[c] + alpha[a] + alpha[b]
            cba=alpha[c] + alpha[b] + alpha[a]
            key = alpha[a] + alpha[b] + alpha[c]
            list=[abc, acb, bac, bca, cab, cba]
            dict[key]=list
count = count * 6

#导出
path = r"C:\Users\lxr\Desktop\字母排列.txt"
with open(path, "a+") as f:
    # 遍历建和值
    f.write("以下内容格式为 abc(26个字母挑选的3个字母) : [它的排列顺序]\n")
    f.write("count = {:^4} \n".format(count))
    f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
    for k, v in dict.items():
        hao=">>"
        r = "{:^4}\t{:^4}\t{:^5}\t{:^5}\t{:^5}\t{:^5}\t{:^5}\t{:^5}\n".format(k, hao, v[0], v[1], v[2], v[3], v[4], v[5])
        f.write(r)
    f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
    f.write("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n")
    f.write("导出成功！\n")

print("导出成功！")
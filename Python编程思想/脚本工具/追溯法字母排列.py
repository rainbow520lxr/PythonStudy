'''

追溯法深度优先
追溯法可以解决排列组合的问题
追溯发

'''
x = ["a", "b", "c",
         "d", "e", "f",
         "g", "h", "i",
         "j", "k", "l",
         "m", "n", "o",
         "p", "q", "r",
         "s", "t", "u",
         "v", "w", "x",
         "y", "z"]

n = 2
list= []


def swap(x, a, b):
    temp = x[a]
    x[a] = x[b]
    x[b] = temp

def backtrak(t):
    if t > n:
        list.append(x[0]+x[1]+x[2])
    else:
        for i in range(t,26):
            print("t=",t,"i=",i)
            swap(x, t, i)
            print("第%d轮：x[%d]= %s x[%d] = %s" % (t,t,x[t],i,x[i]))
            backtrak(t+1)
            swap(x, t, i)
            print("第%d轮返回：x[%d]= %s x[%d] = %s" % (t, t, x[t], i, x[i]))
backtrak(0)

print(list)

print("count = ", len(list))














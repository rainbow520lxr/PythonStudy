
''''''
'''
对于list-tuple-dict-set的读取
'''

import pickle  #数据持久性模块
mylist = [1, 2, 3, 4, 5, "lxr is a good man!"]
path = "a.txt"

f = open(path, "wb")
#写入列表
pickle.dump(mylist, f)
f.close()

#读取
templist = []
f1 = open(path, "rb")
templist = pickle.load(f1)
print(templist)
f1.close()
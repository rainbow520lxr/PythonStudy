'''
break语句：
作用：跳出for和while循环

注意：只能跳出距离他最近的那一层循环


'''
for i in range(10):
    print(i)
    if i == 5:
        break
i = 0
while 1:
    i += 1
    print(i)
    if i == 3:break

'''
continue语句
作用：跳过当前循环中的剩余语句，然继续下一次循环
'''

for i in range(10):
    print(i)
    if i== 3:
        continue
    print("*")
    print("nihao")

num = 0

#while中使用continue注意
while num < 10:
    print(num)
    if num == 3:
        num += 1
    print("*")
    num += 1







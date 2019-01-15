''''''
'''

概述：(key-value)存储数据，其具有极快的查找速度

key的特性：
1.字典中的key必须唯一
2.key必须是不可变的对象
3.字符串、整数等都是不可变的，可以作为key
4.list是可变的，不能作为key

例子：保存多位学生的姓名与成绩

使用字典
'''

dict = {"tom":10, "lilei":20, "lxr":100}

#元素的访问
#获取：字典名[key]
print(dict["lxr"])
# print(dict["sunk"])#没有会报错
#数据获取get(["sunk"])没有返回None不报错
if dict.get("sunk") == None:
    print("字典中没有这个建")

#添加
dict["lxy"] = 90
print(dict)
#因为一个key对应一个value所有多次对一个key的value赋值，其实就是修改值

#删除,仅名字相同的pop与列表
dict.pop("lxr")
print(dict)

#遍历建
for key in dict:
    print(key, dict[key])

#遍历值
for value in dict.values():
    print(value)

#遍历建和值
for k,v in dict.items():
    print(k,":",v)

#本来存入字典内存中都是无序的，但在枚举的方法后就会自动以存入的顺序排序
for i ,v1 in enumerate(dict):
    print(i, v1)

#查找和插入的速度极快，不会随着key-value的增加而变慢
#需要占用大量的内存，内存浪费多

#list的查找和插入的速度会随着数据量的曾都而减慢，
# 占用空间小，浪费内存少




'''
因为字符串不能对原本的地址中做修改，
但可以新建一个被替换的一部分的字符串
'''
str = "lxr is a good good man!"
str1 = str.replace("good", "nice", 1)
print(str)
print(str1)

#创建一个字符串映射表  翻译文本的
t = str.maketrans("ab", "cd")  #第一个是要转的字符串， 第二个是目标字符串
#替换方式是 a=c b=d
str = "lxr is a good good man!"
str1 = str.translate(t)
print(str)
print(str1)


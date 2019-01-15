import tkinter

win = tkinter.Tk()
win.title("lxr")
win.geometry("400x400+200+20")


'''
输入控件
用于显示简单的文本内容
'''
'''
列表框控件，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串

'''
#1.创建一个listbox,添加几个元素
lb = tkinter.Listbox(win,
                     selectmode=tkinter.BROWSE#选择一个模式
                     )
for item in ["nihao", "nice", "handsome"]:
    lb.insert(tkinter.END, item) #按顺序添加

#在开始添加
#在头添加
lb.insert(tkinter.ACTIVE, "cool")
#
lb.insert(tkinter.END, ["aadad", "asdasd", "asdasssssss"])
#删除 参数1为开始的索引， 参数2为结束的索引， 如果不指定参数2， 只删除第一个索引的内容
# lb.delete(1, 3)
lb.delete(1)
lb.pack()
#选中
lb.select_set(0, last=3) #参数1是开始索引，参数二为结束的索引
#取消选中
lb.select_clear(1, 2)  #参数1是开始索引，参数二为结束的索引
#获取到列表中元素的个数
print(lb.size())
#获取列表中的内容
print(lb.get(2, 4))
#获取当前的索引项，不是item元素
print(lb.curselection())
#判断一个选项是否被选中
print(lb.select_includes(1))
print(lb.select_includes(3))


win.mainloop()
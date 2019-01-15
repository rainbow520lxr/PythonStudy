import tkinter

win = tkinter.Tk()
win.title("lxr")
win.geometry("400x400+200+20")


'''
输入控件
用于显示简单的文本内容
'''
#绑定变量
lbv = tkinter.StringVar()
#与Browser相似，但不支持鼠标移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)

for item in ["nihao", "nice", "handsome"]:
    lb.insert(tkinter.END, item) #按顺序添加



#1.打印当前列表中的选项
print(lbv.get())
#2.设置选项
lbv.set(("1", "2", "3"))
#3.绑定事件
def myPrint(event):
    print(lb.curselection())
#给这个列表绑定事件
lb.bind('<Double-Button-1>', myPrint)

lb.pack()

win.mainloop()
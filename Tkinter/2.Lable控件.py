import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("lxr")
#设置大小和位置
win.geometry("400x400+200+200")

#进入消息循环
'''
Lable：标签空间可以显示文本
'''
#win 父窗体
lable = tkinter.Label(win,
                      text="lxr is a good man",
                      bg="pink",
                      fg="red",
                      font=("黑体", 15),
                      width=10,
                      height=2)
#显示出来
lable.pack()

win.mainloop()
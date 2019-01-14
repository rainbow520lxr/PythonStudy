import tkinter

win = tkinter.Tk()
win.title("lxr")
win.geometry("400x400+200+20")


'''
输入控件
用于显示简单的文本内容
'''

#绑定变量
e = tkinter.Variable()

entry = tkinter.Entry(win, textvariable=e)
#在这之后就代表输入框的这个对象
#设置值
e.set("lxr is a good man")
#取值
print(e.get()) #或者print(entry.get())

entry1 = tkinter.Entry(win, show ="*")#密文显示
entry.pack()
entry1.pack()

win.mainloop()
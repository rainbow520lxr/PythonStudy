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
button = tkinter.Button(win, text="按钮", command=lambda:print(e.get()))



entry.pack()
button.pack()


win.mainloop()
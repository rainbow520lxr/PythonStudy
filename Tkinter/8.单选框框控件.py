import tkinter

win = tkinter.Tk()
win.title("lxr")
win.geometry("400x400+200+20")


'''
输入控件
用于显示简单的文本内容
'''

'''单选框
一组单选框要绑定一个变量
'''

r = tkinter.IntVar()


radio1 = tkinter.Radiobutton(win, text="one", value=1, variable=r, command=lambda :print(r.get()))
radio2 = tkinter.Radiobutton(win, text="two", value=2, variable=r, command=lambda :print(r.get()))
radio3 = tkinter.Radiobutton(win, text="three", value=3, variable=r, command=lambda :print(r.get()))

radio1.pack()
radio2.pack()
radio3.pack()



win.mainloop()
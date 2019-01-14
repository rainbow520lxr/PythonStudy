import tkinter

win = tkinter.Tk()
win.title("lxr")
win.geometry("400x400+200+20")


'''
输入控件
用于显示简单的文本内容
'''
hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()

def updata():
    message = ""
    if hobby1.get()==True:
        message += "money\n"
    if hobby2.get()==True:
        message += "money1\n"
    if hobby3.get()==True:
        message += "money2\n"
    text.delete(0.0, tkinter.END)  #从0行0列开始清楚到最后
    text.insert(tkinter.INSERT, message)





check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=updata)
check1.pack()
check2 = tkinter.Checkbutton(win, text="money1", variable=hobby2, command=updata)
check2.pack()
check3 = tkinter.Checkbutton(win, text="money2", variable=hobby3, command=updata)
check3.pack()
text = tkinter.Text(win,width=30, height=4)
text.pack()



win.mainloop()
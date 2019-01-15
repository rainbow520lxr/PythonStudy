import tkinter

def fun():
    print("lxr is a good man!")



win = tkinter.Tk()
win.title("lxr")
win.geometry("400x400+200+20")

#创建按钮
button1 = tkinter.Button(win,
                        text = "按钮",
                        command= fun,#这里不加括号
                        width=10,
                        height=10,
                        )
button2 = tkinter.Button(win,
                        text = "按钮",
                        command= lambda:print("lxr is a good man"),
                        width=10,
                        height=10,
                        )
button3 = tkinter.Button(win,
                        text = "按钮",
                        command= win.quit,
                        width=10,
                        height=10,
                        )
button1.pack()
button2.pack()
button3.pack()
win.mainloop()
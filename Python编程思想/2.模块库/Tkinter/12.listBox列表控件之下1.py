import tkinter

win = tkinter.Tk()
win.title("lxr")
win.geometry("400x400+200+20")

'''
用于显示简单的文本内容
输入控件
'''
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)

lb.pack()



for item in ["nihao", "nice", "handsome", "cad", "nihao", "nice", "handsome", "cad", "nihao", "nice", "handsome", "cad"]:
    lb.insert(tkinter.END, item) #按顺序添加


win.mainloop()
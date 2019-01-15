import tkinter

win = tkinter.Tk()
win.title("lxr")
# win.geometry("400x400+200+20")

'''
用于显示简单的文本内容
输入控件
'''
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)
#按住shift + 可以实现连选
#按住cntrol，可以实现多选
#创建滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side = tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side = tkinter.LEFT, fill=tkinter.BOTH)
sc['command'] = lb.yview


for item in ["nihao", "nice", "handsome", "cad", "nihao", "nice", "handsome", "cad", "nihao", "nice", "handsome", "cad"]:
    lb.insert(tkinter.END, item) #按顺序添加


win.mainloop()
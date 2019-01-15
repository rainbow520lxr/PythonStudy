import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("lxr")
#设置大小和位置
win.geometry("400x400+200+200")

#进入消息循环
'''
text:文本控件，用于显示多行文本
'''

text = tkinter.Text(win, width=30, height=4)  #heigth显示的行数
text.pack()
str = "nasadsadadadasdasdadadasdas"
#插入值
text.insert(tkinter.INSERT, str)


win.mainloop()
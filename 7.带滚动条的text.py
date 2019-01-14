import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("lxr")
#设置大小和位置
# win.geometry("400x400+200+200")

#进入消息循环
'''
text:文本控件，用于显示多行文本
'''
#创建滚动条
s = tkinter.Scrollbar()
text = tkinter.Text(win, width=30, height=4)  #heigth显示的行数
#side放到窗体的那一侧
s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
#关联
s.config(command =text.yview)#滚动条动文本动
text.config(yscrollcommand= s.set)#文本动滚动条动
str = "nasadsadadadasdasdadadasdas"
#插入值
text.insert(tkinter.INSERT, str)


win.mainloop()
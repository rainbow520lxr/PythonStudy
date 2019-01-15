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
                      text="lxr is a good man",#显示文本类容
                      bg="pink",#填充颜色，背景色
                      fg="red",#字体颜色，前景色
                      font=("黑体", 15),#字体大写，类型
                      width=10,#宽
                      height=2,#高
                      wraplengt=30,#指定text文中多宽换行
                      justify="left",#设置换行后的对齐方式
                      anchor="center"#位置n北  e东 s南 w西 center居中 ne se sw nw 默认center
                      )
#显示出来
lable.pack()

win.mainloop()
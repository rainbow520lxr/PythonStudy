#简单绘图绘图工具
#导入turtle库
'''
提供一个小海归，可以理解为一个机器人，只能听得懂有限的命令


该库有三种命令

第一种笔控制命令
绘图窗口的原点(0, 0)在正中间，默认海归的方向是右侧
up()笔抬起不画图可以移动，就好比将笔离开纸面再运动
down()笔落下



第二种运动命令
forward(d)  向前移动d长度
backward(d) 向后一定d长度
right(d)  向右转动d度
left(d)  向左转动d度
goto(x, y) 移动到坐标为（x,y)的位置

speed(speed) 笔画绘制的速度[0, 10]
setheading() 改变海龟的朝向
pensize()笔的粗细宽度
pencolor()笔画的颜色
reset() 恢复所有设置，清空窗口，重置turtle状态
clear() 清空窗口，但turtle的设置不会变

circle( r, steps=e) 绘制一个圆形， 第一个参数是半径， 第二个参数为画多少直线构成一个圆
设置为5则画出5边形
填充必须要一套函数使用
begin_fill()
fillcolor(colorstr)填充颜色

第三种其他命令
done()程序继续执行
undo()撤销
hideturtle()海龟隐藏
showturtle()显示海龟
screensize(x, y)设置画布大小

'''
import turtle as t


t.forward(100)
t.goto(-100, -200)
t.speed(0.1)

t.done()


from tkinter import *  #导入tkinter模块所有内容
root = Tk()          #创建一个Tk根窗口组件root
c = Canvas(root,bg = 'white', width=130, height=70); c.pack()#创建并显示Canvas
c.create_rectangle(10,10,60,60,fill='red')                 #红色填充矩形
c.create_rectangle(70,10,120,60,fill='red',outline='blue',width=5)#蓝色边框红色填充矩形，边框宽度5

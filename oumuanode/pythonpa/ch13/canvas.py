from tkinter import *
root = Tk()                                   #创建1个Tk根窗口组件root
c = Canvas(root,bg = 'yellow', width=200, height=100);#创建200×100、背景为黄色的画布
c.pack()                            #调用组件的pack方法，调整其显示位置和大小

from tkinter import *           #导入tkinter模块所有内容
root = Tk();  root.title("LabelFrame")    #创建1个Tk根窗口组件。设置root窗口标题
lf = LabelFrame(root, text="组1") #创建LabelFrame组件对象
lf.pack()          #调用pack方法，调整其显示位置和大小
Button(lf, text="确定").pack(side=LEFT)  #确定按钮，左停靠
Button(lf, text="取消").pack(side=LEFT)  #取消按钮，左停靠
root.mainloop()    #调用组件的mainloop方法，进入事件循环

from tkinter import *            #导入tkinter模块所有内容
root = Tk();  root.title("选择项")  #窗口标题
v = StringVar(root)
v.set('Python')
om = OptionMenu(root,v,'Python','Perl','JavaScript','C#')
om['width']=10     #宽度10
om['anchor']=W    #设置停靠对齐方式
om.pack()        #调用pack方法，调整其显示位置和大小
root.mainloop()   #调用组件的mainloop方法，进入事件循环   

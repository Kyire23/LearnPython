from tkinter import *  # 导入tkinter模块所有内容

root = Tk();
root.title("Button")  # 窗口标题
w = Button(root, text="确定")  # 创建Button组件对象，显示文本为"确定"
w.config(state=DISABLED)  # 设置Button组件的状态为禁用
w['width'] = 20  # 设置宽度
w.pack()  # 调用pack方法，调整其显示位置和大小
root.mainloop()  # 调用组件的mainloop方法，进入事件循环

a=[]                        #初始化列表
x=float(input("请输入一个实数，输入-1终止："))
while x != -1:
    a.append(x)               #将所输入的实数添加到列表中
    x=float(input("请输入一个实数，输入-1终止："))
print(len(a), sum(a), sum(a)/len(a))       

m=int(input("请输入整数m：")); n=int(input("请输入整数n："))
while(m!=n):
    if (m > n): m=m-n
    else: n=n-m
print(m)

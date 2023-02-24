h=100.0;s = h; r=h/2; #第一次。s表示路程之和，r表示反弹距离
for i in range(2,11): #第2-10次
    s += r*2; r = r / 2
print(str.format("小球在第10次落地时，共经过{0}米",s)) 
print(str.format("第10次反弹{0}米",r))

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{0}*{1}={2}".format(i,j,i*j).ljust(8),end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print('*',end=' ')
#     print()

# for i in range(1,6):
#     print('*',end=' ')
#

# for i in range(1,6):
#     for j in range(6-i):
#         print('*',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print(' ',end=' ')
#     for z in range(i):
#         print('*',end=' ')
#     for t in range(i):
#         print('*',end=' ')
#
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print(' ',end=' ')
#     for z in range(6-i):
#         print('*',end=' ')
#     print()

# for i in range(1, 7):
#     for j in range(7 - i - 1):
#         print(' ', end=' ')
#     for z in range(2 * i - 1):
#         print('*', end=' ')
#
#     print()

# #猜拳小游戏
# #建立一个无限循环
# while True:
#     print('*******************************************************')
#     print('---------------------欢迎进入游戏-----------------------')
#     print('输入对应的数字进行出拳')
#     print('1,是剪刀 2,是石头 3,是布')
#     user1 = int(input('请玩家1出拳:'))#提示玩家1出拳
#     print('########################################################')
#     user2 = int(input('请玩家2出拳:'))#提示玩家二出拳
# #判断输赢条件
#     if (user1==1 and user2==2) or (user1==2 and user2==3) or (user1==3 and user2==1):
#         print('玩家2获胜')
#         print('玩家1不要气馁哦')
#     elif user1 == user2:
#         print('平局')
#     elif (user1 >3 ) or (user2 > 3) or (user1 < 1) or (user2 < 1):
#         print('出错了需要重新运行程序哦')
#         break
#     else:
#         print('玩家1获胜')
#         print('玩家2不要气馁哦')

import random # 调用random模块
# 1,用户自己出拳
user=int(input('请出拳: 1(剪刀) 2(石头) 3(布)'))
# 2，电脑出拳
computer=random.randint(1,3) #随机产生1—3之间的随机数
# 3，判断胜负
if user==computer:
    print('平局')
elif (user==1 and computer==3) or (user==2 and computer==1) or (user==3 and computer==2):
    print('玩家胜利')
else:
    print('电脑胜利')

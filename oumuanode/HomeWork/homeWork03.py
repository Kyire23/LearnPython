# import random
# # 1.从控制台输入所要出的拳—— 石头1 剪刀2 布3
# print('**************欢迎来带猜拳游戏，一锤定音**************')
# player =int(input("请输入您要出的券(石头1 剪刀2 布3):"))
#
# # 2.电脑随机出拳
# computer = random.randint(1,3)
# print("玩家选出的拳头是%s,电脑出的拳头是%d" % (player,computer))
#
# # 3.比较胜负
# # 石头 剪刀  石头胜利
# # 石头 布    布胜利
# # 剪刀 布    剪刀胜利
# if player>=1 or player<=3:
#     if ((player==1 and computer==2)
#             or (player==2 and computer==3)
#             or (player==3 and computer==1)):
#         print("欧耶，玩家player胜利")
#
#     elif (player==computer):
#         print("再来一局")
#     else:
#         print("电脑胜利，不服气！")
# else:
#     print("玩家输入不合法哦")

#
# mydict={}
# count = 0
# for i in input("英文句子:\n").split():
#     if i in mydict:
#         mydict[i]+=1
#     else:
#         mydict[i]=1
#     count+=1
# for key,value in mydict.items():
#     print(key,value)
# print('共有{}个单词'.format(count))

s = [9,7,8,3,2,1,55,6]
sum = 0
all = 0
maxnum = max(s)
minnum = min(s)
for i in s:
    sum +=1
    all +=1
average = all/sum
print(str("元素个数{0},最大值{1},最小值{2},元素和{3},平均值{4}").format(sum,maxnum,minnum,all,average))










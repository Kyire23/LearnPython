import random
def gamble(stake, trials):
    """返回输掉stake所需要的次数，模拟仿真trials次取平均值"""
    total_bets = 0      #总下注次数
    max_cash = stake    #最大赌资
    for t in range(trials):#模拟trials次取平均
        cash = stake  #筹码
        while cash > 0: #持续下注直到破产
            #模拟一次下注
            total_bets += 1
            if random.randrange(0, 2) == 0:
                cash += 1
                max_cash = max(max_cash, cash)
            else: cash -= 1
            #print(cash)
    #print("赌博过程中最大赌资={}".format(max_cash))
    return int(total_bets/trials)
if __name__ == "__main__":
    print(gamble(1,100),gamble(5,100),gamble(10,100),gamble(20,100))

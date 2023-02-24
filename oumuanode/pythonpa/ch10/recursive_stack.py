def vertical(n):
    """依次垂直输出整数的各数字"""
    if n < 10: #基本情况：n为1位数时，直接输出
        print(n)
    else: #递归情况：多位数时，整除10后递归调用
        vertical(n//10)
        print(n%10) #输出余数
if __name__ == "__main__":
    vertical(687)

import os, re
def check_email(strEmail):
    regex_email = re.compile(r'^[\w\.\-]+@([\w\-]+\.)+[\w\-]+$')
    result = True if regex_email.match(strEmail) else False
    return result
#测试代码
if __name__=='__main__':
    str1 = input("请输入电子邮箱：")
    print( check_email(str1))
   

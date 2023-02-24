import requests
query = input("你喜欢谁？")
url = 'https://sogou.com/web?query=query'
dic = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp=requests.get(url,headers=dic)
print(resp)
#查看源码
print(resp.text)
# from urllib.request import urlopen
#
# url="http://www.baidu.com"
# resp=urlopen(url)
# #print(resp.read().decode("utf-8"))
#
# with open("mybaidu.html",mode='w',encoding="utf-8") as f:
#     f.write(resp.read().decode("utf-8"))
# print("over!")


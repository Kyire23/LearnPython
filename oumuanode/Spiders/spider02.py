import re
import requests

url = "https://movie.douban.com/top250"
#获取源代码
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=headers)
page_content=resp.text
#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>',re.S)
result = obj.finditer(page_content)
for it in result:
    print(it.group("name"))
# obj = re.compile(r"\d+")
# ret = obj.finditer("电话是10010，他的电话11234")
# for it in ret:
#     print(it.group())
import json
urls={'baidu':'http://www.baidu.com/',
      'sina':'http://www.sina.com.cn/',
      'tencent':'http://www.qq.com/',
      'taobao':'https://www.taobao.com/'}
with open(r'c:\pythonpa\data.json', 'w') as f:
    json.dump(urls, f)

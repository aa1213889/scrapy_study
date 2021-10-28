import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

post_data = {
    'kw': 'dog'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# post请求参数必须要进行编码
post_data = urllib.parse.urlencode(post_data).encode('utf-8')

# urllib.request.Request data参数为post请求参数
request = urllib.request.Request(url=url, data=post_data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')
print(json.loads(content))

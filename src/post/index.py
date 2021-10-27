import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

post_data = {
    'kw': 'dog'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# urllib.request.Request data参数为post请求参数
request = urllib.request.Request(url=url, data=post_data, headers=headers)

# urlopen 可以传入一个Request的对象
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

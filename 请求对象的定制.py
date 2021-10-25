from http.client import responses
import urllib.request

url = 'https://www.baidu.com/'

# User-Agent:用户代理来证明自己是普通用户，加上后可以绕过反爬机制
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# Request()的第三个参数才是headers，所以需要赋值一下，不然会默认为第二个参数
request = urllib.request.Request(url, headers=headers)

# urlopen 可以传入一个Request的对象
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

import urllib.request
import random

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

# 代理池 模拟的i数据
proxies_pool = [
    {'http': '1.71.143.122:6969'},
    {'http': '2.71.143.122:6969'},
    {'http': '3.71.143.122:6969'},
    {'http': '4.71.143.122:6969'},
    {'http': '5.71.143.122:6969'},
]
# random.choice 随机从数组选择一个
proxies = random.choice(proxies_pool)

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

fp = open('proxy.html', 'w', encoding='utf-8')
fp.write(content)
fp.close()

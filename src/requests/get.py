import requests

url = 'https://www.baidu.com/s?'
data = {'wd': '北京'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

response = requests.get(url=url, params=data, headers=headers)
print(response.text)
# 参数不需要urlencode编码 不需要请求对象定制

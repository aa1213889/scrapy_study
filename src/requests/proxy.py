import requests

url = 'https://www.baidu.com/s?'
data = {'wd': 'ip'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

proxy = {
    'https': '111.111.111.111:1111'
}

response = requests.get(url=url, params=data, headers=headers, proxies=proxy)

with open('proxy.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)

import urllib.request


url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

# proxies 代理的ip地址+端口号  https://www.kuaidaili.com/free/inha/5/
proxies = {
    'http': '1.71.143.122:6969'
}
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)


content = response.read().decode('utf-8')

fp = open('proxy.html', 'w', encoding='utf-8')
fp.write(content)
fp.close()

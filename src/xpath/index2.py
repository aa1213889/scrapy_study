# 在线爬取百度源码
from lxml import etree
import urllib.request


url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',

}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 1.解析响应文件
html = etree.HTML(content)

# 2.获取响应数据
result = html.xpath('//input[@id="su"]/@value')

print(result)  # ['百度一下']

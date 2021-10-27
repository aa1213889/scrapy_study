import urllib.request
import urllib.parse

# 计算机需要讲中文解析为Unicode编码的英文字符
# 周杰伦 三个字 Unicode编码 的 %E5%91%A8%E6%9D%B0%E4%BC%A6
# parse.quote 将汉字转为Unicode编码
name = urllib.parse.quote('周杰伦')
url = 'https://www.baidu.com/s?wd=' + name

# 当查询的条件多的时候 可以使用parse.urlencode(字典)
parse_data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}
# wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE
print(urllib.parse.urlencode(parse_data))


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# urlopen 可以传入一个Request的对象
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

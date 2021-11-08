# get请求
# 获取豆瓣电影的第一页数据并保存

import urllib.request


# 1.请求对象定制
url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# 2.获取响应数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)


# 3.数据下载本地
fp = open('douban-hot.json', 'w', encoding='utf-8')
fp.write(content)
fp.close()

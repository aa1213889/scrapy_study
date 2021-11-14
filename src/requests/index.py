import requests

url = 'https://www.baidu.com/'

response = requests.get(url=url)
response.encoding = 'utf-8'

# 返回网页源码
print(response.text)

# 返回二进制源码
print(response.content)

# 返回响应状态码
print(response.status_code)

# 返回响应头
print(response.headers)

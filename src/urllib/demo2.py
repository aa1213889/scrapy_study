import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
print(type(response))  # <class 'http.client.HTTPResponse'>

# getcode() 返回状态码
print(response.getcode())  # 200

# geturl() 返回url地址
print(response.geturl())  # http://www.baidu.com

# getheaders() 返回响应头信息
print(response.getheaders())

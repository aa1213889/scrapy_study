import urllib.request

# 1.定义一个url
url = 'http://www.baidu.com'

# 2.模拟浏览器向服务器请求
response = urllib.request.urlopen(url)

# 3.获取响应中的页面源码
# read() 返回的字节形式的二进制数据
# 需要将二进制数据转为字符串 ---> 解码
# 解码 decode('编码的格式')
content = response.read().decode('utf-8')

# 打印
print(content)

# 获取weibo.cn的网页内容
# 1. 先正常登录微博
# 2.登录成功后在第一个get请求接口里找到cookie和referer两个请求头

# cookie中携带者你的登录信息，如果有登录之后的cookie，那就可以携带着cookie进入任何页面
# referer：判断当前路径是不是由上一个路径进来的 一般情况下是做图片防盗链

import urllib.request


url = 'https://weibo.cn/1686546714/info'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'cookie': '_ga=GA1.2.227238778.1628340814; SCF=ArRnGceIlyAF-7-wfdFg4JmLmpk_xzrOQ0HOeRggk1hjKltlr7szRFtPQMDfydLBf2bv86wrwWNa1hETqQisqH4.; SUB=_2A25MjTkdDeRhGeRO7VoV-C_Iwz-IHXVvjkdVrDV6PUJbktCOLRLtkW1NUHK4PXUew2UuB4nI_dLvCASDNtZjy4sw; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF7wmXdH8muR3rbIYw9F.jG5JpX5K-hUgL.Foz7SonX1h2X1he2dJLoIpqLxK.L1h-LBo2LxKqLBo2L1h8kPfvk; SSOLoginState=1636387149; ALF=1638979149; _T_WM=304020ffa83fb93c7b39d8e16cfe9f9c',
    'referer': ' https://weibo.cn/1686546714/info'
}

request = urllib.request.Request(url=url, headers=headers)


response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')


fp = open('weibo.html', 'w', encoding='utf-8')
fp.write(content)
fp.close()

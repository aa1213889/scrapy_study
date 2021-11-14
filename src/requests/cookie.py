import requests
from lxml import etree

# 1.在该网站的登陆页面 随意输错帐号密码 观察登录的接口需要的参数

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# 2.古诗词网的登录页面的URL
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
login_response = requests.get(url=login_url,  headers=headers)
login_content = login_response.text
html = etree.HTML(login_content)

# 3. 该网站登录的接口需要7个参数
# __VIEWSTATE、__VIEWSTATEGENERATOR、from、email、pwd、code、denglu

# 3.1 __VIEWSTATE、__VIEWSTATEGENERATOR 两个值在HTML页面的对应input框的属性上，可以通过HTML源码找到
__VIEWSTATE = html.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = html.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]

# 3.2 下载验证码 并观察值   (也可以使用收费的验证码识别平台---超级鹰等等)
code_img_url = html.xpath('//img[@id="imgCode"]/@src')[0]
code_url = 'https://so.gushiwen.cn' + code_img_url
# 下载图片 图片是二进制 使用response.content 而不是response.text
session_requests = requests.session()
code_response = session_requests.get(code_url)
# wb:写入二进制数据
with open('./src/requests/gushiwen_code_img.jpg', 'wb') as fp:
    fp.write(code_response.content)
code = input('please input your code')


# 4. 点击登录
login_api = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code': code,
    'denglu': '登录'
}

login_response = session_requests.post(url=code_url, headers=headers, data=data_post)
with open('./src/requests/gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(login_response.text)

from selenium import webdriver

# 1.创建浏览器操作对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 2.访问网站
url = 'https://www.jd.com/'
browser.get(url)

# 3.获取源码
content = browser.page_source
print(content)

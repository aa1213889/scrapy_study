from selenium import webdriver

# 1.创建浏览器操作对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# 2.访问网站
url = 'http://www.baidu.com/'
browser.get(url)

# 3.获取源码
content = browser.page_source

# 根据id来找对象 也可以class tag等等
button = browser.find_element_by_id('su')
print(button)

# 使用xpath语法 elements多个 数组形式
xButton = browser.find_element_by_xpath('//input[@id="su"]')
print(xButton)

# 拿取标签的属性值
input = browser.find_element_by_id('su')
print(input.get_attribute('class'))
print(input.tag_name('class'))

from selenium import webdriver
import time

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'http://www.baidu.com/'
browser.get(url)

# 睡眠2s
time.sleep(2)

# 1.文本框赋值
input = browser.find_element_by_id('kw')
input.send_keys('周杰伦')
time.sleep(2)

# 2.模拟点击
button = browser.find_element_by_xpath('//input[@id="su"]')
button.click()
time.sleep(2)

# 3.滚动条滚动到最下 execute_script执行JS代码
scroll_js = 'document.documentElement.scrollTop = 100000'
browser.execute_script(scroll_js)
time.sleep(2)

# 4.点击下一页
n_a = browser.find_element_by_xpath('//a[@class="n"]')
n_a.click()
time.sleep(2)

# 5.回到上一页
browser.forward()
time.sleep(2)

# 6. 退出
browser.quit()

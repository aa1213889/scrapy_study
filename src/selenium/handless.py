from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# chrome_path 谷歌浏览器主文件路径 其他配置都是默认必须要添加的
def share_browser(chrome_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.binary_location = chrome_path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


browser = share_browser('C:\Program Files\Google\Chrome\Application\chrome.exe')

url = 'https://www.jd.com/'
browser.get(url)

content = browser.page_source
print(content)

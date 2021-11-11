# 在线爬取站长之家 并拿去指定图片
from lxml import etree
import urllib.request


def task_start(start_page, end_page, key_word):
    for page in range(start_page, end_page+1):
        create_request(page, key_word)


def create_request(page, key_word):
    url = 'https://aspx.sc.chinaz.com/query.aspx?keyword=' + \
        urllib.parse.quote(key_word) + \
        '&issale=&classID=11&navindex=0&page=' + str(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    get_img_src(content)


def get_img_src(content):
    html = etree.HTML(content)
    img_arr = html.xpath('//div[@id="ulcontent"]//img/@data-src')
    name_arr = html.xpath('//div[@id="ulcontent"]//img/@alt')
    for index in range(len(img_arr)):
        img_url = 'https:' + img_arr[index]
        flie_name = './src/chinaz/img/' + name_arr[index] + '.jpg'
        urllib.request.urlretrieve(url=img_url, filename=flie_name)


task_start(1, 1, '狗')

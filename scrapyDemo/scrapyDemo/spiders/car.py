import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']

    # 如果请求接口是html为结尾的 结尾不需要加“/”
    start_urls = ['http://https://car.autohome.com.cn/price/brand-15.html/']

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        for name in name_list:
            print(name.extract())

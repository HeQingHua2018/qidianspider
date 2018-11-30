
import scrapy
from scrapy.selector import Selector


class QiDianSpider(scrapy.spiders.Spider):
    # 启动项目指定的name参数
    name = 'qidian'
    # 需要爬取那些页面
    start_urls = {
        'https://www.qidian.com/',
    }

    def parse(self, response):
        print(response)
        # 页面源码
        # print(response.body)
        res = Selector(response)
        menu_type = res.xpath('//*[@id="classify-list"]/dl/dd/a/cite/span/i/text()').extract()
        menu_type_href = res.xpath('//*[@id="classify-list"]/dl/dd/a/@href').extract()
        print(menu_type, menu_type_href)
        return menu_type, menu_type_href




import scrapy
from scrapy.selector import Selector
from qidianspider.items import DouBanSpiderItem


class DouBanSpider(scrapy.spiders.Spider):
    name = 'douban'
    start_urls = {
        'https://movie.douban.com/top250',
    }

    def parse(self, response):

        res = Selector(response)
        items = DouBanSpiderItem()
        # 电影名
        items['name'] = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()').extract()
        # 电影的图片
        items['avator'] = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src').extract()
        # 电影导演和主演
        director_info = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[1]').extract()
        items['director'] = [info.strip().replace('\xa0', '') for info in director_info]

        # 年份/国家/类型
        movie_info = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[2]').extract()
        movie_info = [info.strip().replace('\xa0', '') for info in movie_info]
        items['year'], items['guojia'], items['classfication'] = [], [], []
        for info in movie_info:
            items['year'].append(info.split('/')[0])
            items['guojia'].append(info.split('/')[1])
            items['classfication'].append(info.split('/')[2])
        # 评分
        items['rate'] = res.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()').extract()
        return items





# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouBanSpiderItem(scrapy.Item):
    name = scrapy.Field()
    avator = scrapy.Field()
    director = scrapy.Field()
    year = scrapy.Field()
    guojia = scrapy.Field()
    classfication = scrapy.Field()
    rate = scrapy.Field()

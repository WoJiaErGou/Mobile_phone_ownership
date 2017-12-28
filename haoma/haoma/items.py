# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HaomaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #号码
    number = scrapy.Field()
    #运营商
    Corp = scrapy.Field()
    #省份
    Province = scrapy.Field()
    #城市
    City = scrapy.Field()
    #邮编
    AreaCode = scrapy.Field()
    #json返回数据
    Json_data = scrapy.Field()
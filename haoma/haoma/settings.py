# -*- coding: utf-8 -*-

# Scrapy settings for haoma project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'haoma'

SPIDER_MODULES = ['haoma.spiders']
NEWSPIDER_MODULE = 'haoma.spiders'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1
unicom = ['130','131','132','145','155','156','185','186','176','175','166']
mobile1 = ['134','135','136','137','138','147','150','151','178']
mobile2 = ['152','157','158','159','182','183','187','188','198']
telecom = ['133','153','180','181','189','177','173','149','199']
FIELDS_TO_EXPORT = [
    'number',
    'Corp',
    'Province',
    'City',
    'AreaCode',
    'Json_data'
]
MONGO_HOST = "172.28.171.13"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "HAOMA"  # 库名
MONGO_COLL = "haoma_Telecom"  # 电信
# MONGO_COLL = "haoma_Unicom"  # 联通
# MONGO_COLL = "haoma_mobile1"  # 移动
ITEM_PIPELINES = {
    'haoma.pipelines.CSVPipeline':200,
    'haoma.pipelines.MongoPipeline':190,
}
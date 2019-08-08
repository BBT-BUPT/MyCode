# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    count = scrapy.Field()
    uniName = scrapy.Field()
    year = scrapy.Field()
    top = scrapy.Field()
    low = scrapy.Field()
    avreage = scrapy.Field()
    stuNum = scrapy.Field()
    order = scrapy.Field()


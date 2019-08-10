# -*- coding: utf-8 -*-
import scrapy
from FileSpider.items import FilespiderItem

class FilespiderSpider(scrapy.Spider):
    name = 'filespider'
    #allowed_domains = ['ximalaya.com']
    start_urls = ['https://www.ximalaya.com/xiangsheng/9723091/']

    def parse(self, response):
            li_list = response.xpath('//*[@id="anchor_sound_list"]/div[2]/ul/li')
            for li in li_list:
                print(li)
                item = FilespiderItem()
                filename = li.xpath('./div[2]/a/@title').extract_first()
                file_url ="https://www.ximalaya.com" + li.xpath('./div[2]/a/@href').extract_first()
                item["filename"] = filename
                item["file_url"] = "https://fdfs.xmcdn.com/group30/M02/3F/24/wKgJXlmBkwCSsyRnAOw4HLy7JKU631.m4a"
                yield item

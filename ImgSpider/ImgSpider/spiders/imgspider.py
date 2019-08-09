# -*- coding: utf-8 -*-
import scrapy
from ..items import ImgspiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'imgspider'
    keyword = 'girl' #设置英文关键词
    pageMax = 3
    pageNum = 0
    #allowed_domains = ['s,taobao.com']
    start_urls = ['https://pixabay.com/images/search/{}/'.format(keyword)]

    def parse(self, response):
        img_list = response.xpath('//div[@class="item"]/a/img/@data-lazy').extract()
        for img in img_list:
            print(img)
            item = ImgspiderItem()
            item["src"] = [img]
            yield item
        self.pageNum +=1
        nextpage = 'https://pixabay.com/images/search/girl/?pagi={}'.format(self.pageNum+1)
        print(nextpage)
        if self.pageNum < self.pageMax:
            yield scrapy.Request(url = nextpage,callback=self.parse)




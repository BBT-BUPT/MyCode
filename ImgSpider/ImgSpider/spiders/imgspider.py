# -*- coding: utf-8 -*-
import scrapy
from ..items import ImgspiderItem

class ImgspiderSpider(scrapy.Spider):
    name = 'imgspider'
    keyword = 'beautiful girl' #设置英文关键词
    pageMax = 3
    pageNum = 0
    picNum = 1
    #allowed_domains = ['s,taobao.com']
    start_urls = ['https://pixabay.com/images/search/{}/'.format(keyword)]

    def parse(self, response):
        img_list = response.xpath('//div[@class="item"]/a/img/@data-lazy').extract()
        for img in img_list:
            print(img)
            item = ImgspiderItem()
            item["src"] = [img]
            item["name"] = self.keyword+"_{}".format(self.picNum)
            self.picNum +=1
            yield item
        self.pageNum +=1
        nextpage = 'https://pixabay.com/images/search/{}/?pagi={}'.format(self.keyword,self.pageNum+1)
        print(nextpage)
        if self.pageNum < self.pageMax:
            yield scrapy.Request(url = nextpage,callback=self.parse)




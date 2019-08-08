# -*- coding: utf-8 -*-
import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    counter = 1
    uniNum = 1
    uniMax = 10
    #allowed_domains = ['']
    start_urls = ['http://college.gaokao.com/school/tinfo/1/result/31/1/']

    def parse(self, response):
        tr_list = response.xpath('//*[@id="pointbyarea"]/table/tr')[1::]
        uniname = response.xpath('//*[@id="bott"]/div/h2/text()').extract_first()
        for tr in tr_list:
            item = {}
            item['uniName'] = uniname
            item['year'] = tr.xpath('./td[1]/text()').extract_first()
            item['low'] = tr.xpath('./td[2]/text()').extract_first()
            item['top'] = tr.xpath('./td[3]/text()').extract_first()
            item['avreage'] = tr.xpath('./td[4]/a/text()').extract_first()
            item['stuNum'] = tr.xpath('./td[5]/text()').extract_first()
            item['order'] = tr.xpath('./td[6]/text()').extract_first()
            item['count'] = self.counter
            self.counter +=1
            yield item
        self.uniNum += 1
        if self.uniNum <= self.uniMax:
            yield scrapy.Request(
                   url = 'http://college.gaokao.com/school/tinfo/{:}/result/31/1/'.format(self.uniNum)
                   ,callback = self.parse
                )

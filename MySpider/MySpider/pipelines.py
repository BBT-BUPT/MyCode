# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class MyspiderPipeline(object):
    def open_spider(self, spider):
        self.f = open("江西高考历年分数线.csv",'w')
        writer = csv.writer(self.f)
        writer.writerow(["记录序号","年份","录取批次","大学","录取人数","平均分","最高分","最低分"])

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        writer = csv.writer(self.f)
        print(item)
        writer.writerow([item['count'],item['year'],item['order'],item['uniName'],item['stuNum'],item['avreage'],item['top'],item['low']])
        return item

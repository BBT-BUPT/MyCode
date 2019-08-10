# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline

class ImgspiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print(item["src"])
        yield scrapy.Request(item["src"][0])

    def item_completed(self, results, item, info):
        IMAGES_STORE = 'C:\\Users\\19779\\Desktop\\MyCode\\ImgSpider\\'
        image_path = [x["path"] for ok,x in results if ok]
        os.rename(IMAGES_STORE+image_path[0],IMAGES_STORE+"pic\\"+item["name"]+".jpg")


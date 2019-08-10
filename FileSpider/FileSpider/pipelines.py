# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from scrapy.pipelines.files import FilesPipeline
from FileSpider.settings import FILES_STORE

class FilespiderPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        file_url = item['file_url']
        yield scrapy.Request(file_url)

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        os.rename(FILES_STORE + file_paths[0],
                  FILES_STORE  +"full\\"+ item['filename']+'.m4a')
        return item
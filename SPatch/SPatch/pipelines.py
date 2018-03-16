# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpatchPipeline(object):
    def process_item(self, item, spider):
        return item
class SpatchInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open("myurl",'a')
    def close_spider(self, spider):
        self.f.close()
    def process_item(self, item, spider):
        try:
            url_item = item
            self.f.write(url_item)
        except:
            pass
        return item



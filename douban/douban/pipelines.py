# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import  codecs


class DoubanPipeline(object):
    def __init__(self):
        self.file=codecs.open('douban_moive.json',mode='wb',encoding='utf-8')
    def process_item(self, item, spider):
        line ='***'
        str1=item['movie_name']
        line =line+json.dumps(str1,ensure_ascii=False)+'\t'
        line =line+json.dumps(item['movie_score'],ensure_ascii=False)+'\t'
        line =line+json.dumps(item['movie_url'],ensure_ascii=False)+'\n'
        self.file.write(line)
    def close_spider(self,spider):
        self.file.close()

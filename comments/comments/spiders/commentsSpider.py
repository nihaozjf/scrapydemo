# -*- coding: utf-8 -*-
__author__ = 'zhangjufu'
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.selector import Selector
'''
http://www.meituan.com/dianying/yingping/248896/page35
'''
class CommentsSpider(CrawlSpider):
	name="CommentsSpider"
	allowed_domains=['meituan.com']
	start_urls=['http://www.meituan.com/dianying/yingping/248896/page1']
	rules=[
		Rule(sle(allow=('/dianying/yingping/248896/page\d+'),
		         restrict_xpaths=('//li[@class="next"]/a')),
		     callback='parse_item',
		     follow=True)
	]

	def parse_item(self, response):
		print 'parse_item'
		comment=response.xpath('//span[@class="comment__content"]')
		for c in comment.extract():
			print c
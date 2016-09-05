# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import  Selector
from w3c.items import W3CItem

class w3cSpider(scrapy.Spider):
	name='w3c_spider'
	allowed_domains=['w3school.com.cn']
	start_urls=[
		'http://www.w3school.com.cn/xml/xml_syntax.asp'
	]

	def parse(self, response):
		sel=Selector(response)

		sites=sel.xpath('//div[@id="course"]/ul/li')
		for site in sites:
			item = W3CItem()
			title = site.xpath('a/@title').extract()
			link = site.xpath('a/@href').extract()
			desc=site.xpath('a/text()').extract()
			item['title']=title[0]
			item['link']=link[0]
			item['desc']=desc[0]
			print item
			yield  item



# -*- coding: utf-8 -*-
import  scrapy
import string
from scrapy import Selector
from douban.items import  DoubanItem

class DoubanMoiveSpider(scrapy.Spider):
	name='douban_moive_spider'
	allowed_domains=["www.movie.douban.com"]

	start_urls=[
		'https://movie.douban.com/chart'
	]

	def parse(self, response):
		sel=Selector(response)
		movie_name=sel.xpath("//div[@class='pl2']/a/text()").extract()
		'''
		//*[@id="content"]/div/div[1]/div/div/table[3]/tbody/tr/td[2]/div/a/span
		'''
		names=[]
		print '******'
		for name in movie_name[::2]:
			names.append(name.strip().replace('\\',""))
		#print movie_name
		print '******'
		movie_url=sel.xpath("//div[@class='pl2']/a/@href").extract()
		movie_score=sel.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()
		#items = []
		for name ,url,score in zip(names,movie_url,movie_score):
			item=DoubanItem()

		#item['movie_name']=[n.encode('utf-8') for n in movie_name]
		#item['movie_score']=[n for n in movie_score]
		#item['movie_url']=[n for n in movie_url]
			item['movie_name']=name
			item['movie_score']=score
			item['movie_url']=url
			#print item
			yield  item
			#items.append(item)


		#return items
		#print movie_name,movie_score,movie_url
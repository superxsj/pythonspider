# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

quc = []
class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/']



    def parse(self, response):
        urls = response.css('.postlist span a[target*=_blank]::attr(href)').extract()

        for url in urls:
            yield Request(url,callback=self.parse_img)
        #yield Request('http://www.mzitu.com/134304', callback=self.parse_img)
        nexts = response.css('.nav-links a[class*=next]::attr(href)').extract()
        yield Request(nexts, callback=self.parse)

def parse_img(self, response):
        urls = response.css('.main-image img::attr(src)').extract()
        for url in urls:
            print(url)
        next = ''
        index = response.css('.pagenavi a::attr(href)').extract()
        for ind in index:
            next = ind
        #print(next)
        try:
            yield Request(next, callback=self.parse_img)
        except ValueError:
            yield

        #next = response.css('.pagenavi a::attr(href)').extract()
        #yield Request(next, callback=self.parse_img)





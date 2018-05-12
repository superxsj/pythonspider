# -*- coding: utf-8 -*-
import scrapy


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['http://www.mzitu.com']
    start_urls = ['http://http://www.mzitu.com/']

    def parse(self, response):
        pass

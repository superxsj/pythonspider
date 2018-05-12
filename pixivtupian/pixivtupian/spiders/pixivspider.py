# -*- coding: utf-8 -*-
import scrapy


class PixivspiderSpider(scrapy.Spider):
    name = 'pixivspider'
    allowed_domains = ['https://www.pixiv.net']
    start_urls = ['http://https://www.pixiv.net/']

    def parse(self, response):
        pass

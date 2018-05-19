# -*- coding: utf-8 -*-
import scrapy


class PixivspiderSpider(scrapy.Spider):
    name = 'pixivspider'
    allowed_domains = ['www.pixiv.net']
    start_urls = ['https://www.pixiv.net/']

    def parse(self, response):
        print(response.text)

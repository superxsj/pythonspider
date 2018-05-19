# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item ,Field


class tupianItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = Field()
    title = Field()
    image_urls = Field()
    images = Field()
    image_paths = Field()

# class DoubanImgsItem(Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     image_urls = Field()
#     images = Field()
#     image_paths = Field()
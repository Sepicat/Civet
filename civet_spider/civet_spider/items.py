# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CivetSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GtRankUser(scrapy.Item):
    rank = scrapy.Field()
    avatar_url = scrapy.Field()
    username = scrapy.Field()
    name = scrapy.Field()
    location = scrapy.Field()
    language = scrapy.Field()
    repo_cnt = scrapy.Field()
    follower_cnt = scrapy.Field()
    created_date = scrapy.Field(serializer = str)


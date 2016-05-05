# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field

from Logger import *
logger = setupLogging(__name__)
logger.setLevel(DEBUG)


class News(Item):

    title = Field()
    text = Field()

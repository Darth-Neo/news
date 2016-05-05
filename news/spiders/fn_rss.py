# -*- coding: utf-8 -*-
import os
from scrapy.spiders import Spider
from ..items import News

from ..Logger import *
logger = setupLogging(__name__)
logger.setLevel(DEBUG)


class NewsSpider(Spider):
    name = u"news_rss"
    allowed_domains = [u"www.foxnews.com"]
    start_urls = (u'http://feeds.foxnews.com/foxnews/most-popular', )

    def parse(self, response):
        logger.info(u"%s" % response)
        n = 0
        for sel in response.xpath(u'/html'):
            item = News()
            item[u'title'] = sel.xpath(u'//li').extract()
            logger.debug(u"%s%d.parse.item : %20s" % (os.linesep, n, item[u'title']))
            n += 1
            yield item

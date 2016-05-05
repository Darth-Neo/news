# -*- coding: utf-8 -*-
import os
from scrapy.spiders import Spider
from ..items import News

from ..Logger import *
logger = setupLogging(__name__)
logger.setLevel(INFO)


class NewsSpider(Spider):
    name = u"news"
    allowed_domains = [u"www.foxnews.com"]
    start_urls = (
        u'http://www.foxnews.com/trending',
        u'http://feeds.foxnews.com/foxnews/latest',
        u'http://insider.foxnews.com/latest'
    )

    def parse(self, response):
        logger.debug(u"%s" % response)
        n = 0
        for sel in response.xpath(u'/html'):
            item = News()
            item[u'title'] = sel.xpath(u'//div[2]/div/div/div/h2/span/a').extract()
            item[u'text'] = sel.xpath(u'//div[1]/div[2]/ul/li/a/div/h3').extract()
            logger.debug(u"%s%d.parse.item : %20s" % (os.linesep, n, item[u'title']))
            n += 1
            yield item

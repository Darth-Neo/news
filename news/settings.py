#
#  Scrapy settings for news project
#
SPIDER_MODULES = [u'news.spiders']
NEWSPIDER_MODULE = u'news.spiders'
DEFAULT_ITEM_CLASS = u'news.items.News'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = u"User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0"

# ITEM_PIPELINES = {'news.pipelines.FoxnewsPipeline': 1}
ITEM_PIPELINES = {u'news.pipelines.MongoDBPipeline': 1}

MONGODB_SERVER = u"localhost"
MONGODB_PORT = 27017
MONGODB_DB = u"news"
MONGODB_COLLECTION = u"headlines"

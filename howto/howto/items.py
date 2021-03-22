# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HowtoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    course = scrapy.Field()
    excerpt = scrapy.Field()
    category = scrapy.Field()
    bottomhtml = scrapy.Field()
    imgurl = scrapy.Field()
    url = scrapy.Field()
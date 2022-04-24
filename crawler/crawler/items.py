# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Url(scrapy.Item):
    url = scrapy.Field()  # 기사링크
    # last_updated = scrapy.Field(serializer=str)


class Item(scrapy.Item):
    date = scrapy.Field()  # 기사시간
    title = scrapy.Field()  # 기사제목
    article = scrapy.Field()  # 기사본문
    # last_updated = scrapy.Field(serializer=str)

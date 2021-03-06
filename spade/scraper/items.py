"""
Scraped item models.

See http://doc.scrapy.org/topics/items.html

"""
from scrapy.item import Item, Field


class MarkupItem(Item):
    content_type = Field()
    filename = Field()
    headers = Field()
    meta = Field()
    raw_content = Field()
    sitescan = Field()
    urlscan = Field()
    url = Field()
    user_agent = Field()
    redirected_from = Field()

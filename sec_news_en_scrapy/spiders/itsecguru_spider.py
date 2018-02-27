import scrapy
from scrapy import Request, Selector

from sec_news_en_scrapy.items import SecEnNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "itsecguru"
    allowed_domains = ["itsecurityguru.org"]
    start_urls = ['http://www.itsecurityguru.org/category/news/top-10-stories/']

    def parse(self, response):
        topics = []
        for sel in response.xpath('//*[@id="main-content"]/div[@class="content"]/div[@class="post-listing"]/article[@class="item-list"]/h2/a'):
            topic = {'title': sel.xpath('text()').extract(), 'link': sel.xpath('@href').extract()[0], 'src': response.request.url}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecEnNewsItem()
        item['title'] = topic['title'][0]
        item['content'] = "".join(selector.xpath('//*[@id="main-content"]/div[2]/article/div[@class="post-inner"]/div[@class="entry"]/p[*]/text()').extract())
        item['uri'] = topic['link']
        item['src'] = topic['src']
        print('Finish scan title:' + item['title'])
        yield item






import scrapy
from scrapy import Request, Selector

from sec_news_en_scrapy.items import SecEnNewsItem


class HackerNewsSpider(scrapy.Spider):
    name = "hacker_news"
    allowed_domains = ["thehackernews.com"]
    start_urls = ['https://thehackernews.com/']

    def parse(self, response):
        topics = []
        for sel in response.xpath('//*[@id="Blog1"]/div[1]/article[@class="post item module"]/span/h2/a'):
            topic = {'title': sel.xpath('text()').extract(), 'link': sel.xpath('@href').extract(), 'src': response.request.url}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'][0], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecEnNewsItem()
        item['title'] = topic['title'][0]
        item['content'] = "".join(selector.xpath('//*[@id="articlebodyonly"]/div/div/text()').extract())
        item['uri'] = topic['link'][0]
        item['src'] = topic['src']
        print('Finish scan title:' + item['title'][0])
        yield item

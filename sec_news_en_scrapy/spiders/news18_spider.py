import scrapy
from scrapy import Request, Selector

from sec_news_en_scrapy.items import SecEnNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "news18"
    allowed_domains = ["news18.com"]
    start_urls = ['http://www.news18.com/newstopics/cyber-security.html']

    def parse(self, response):
        topics = []
        for sel in response.xpath('//*[@id="main"]/div[8]/div[2]/div[1]/div[@class="search-listing"]/ul/li[*]/h2/a'):
            topic = {'title': sel.xpath('text()').extract(), 'link': sel.xpath('@href').extract(), 'src': response.request.url}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'][0], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecEnNewsItem()
        item['title'] = topic['title'][0]
        item['content'] = "".join(selector.xpath('//*[@id="article_body"]/text()').extract())
        item['uri'] = topic['link'][0]
        item['src'] = topic['src']
        print('Finish scan title:' + item['title'])
        yield item





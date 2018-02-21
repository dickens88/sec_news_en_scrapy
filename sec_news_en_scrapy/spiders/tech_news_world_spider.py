import scrapy
from scrapy import Request, Selector

from sec_news_en_scrapy.items import SecEnNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "tech_news"
    allowed_domains = ["technewsworld.com"]
    start_urls = ['https://www.technewsworld.com/perl/section/tech-security']

    def parse(self, response):
        topics = []
        prefix = "https://www.technewsworld.com"
        for sel in response.xpath('//*[@id="content-main"]/div/table[*]/tr/td[*]/a'):
            topic = {'title': sel.xpath('text()').extract(), 'link': prefix + sel.xpath('@href').extract()[0], 'src': response.request.url}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecEnNewsItem()
        item['title'] = topic['title'][0]
        item['content'] = "".join(selector.xpath('//*[@id="story-body"]/p/text()').extract())
        item['uri'] = topic['link']
        item['src'] = topic['src']
        print('Finish scan title:' + item['title'])
        yield item





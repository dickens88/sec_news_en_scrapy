import scrapy
from scrapy import Request, Selector

from sec_news_en_scrapy.items import SecEnNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "securityweek"
    allowed_domains = ["securityweek.com"]
    start_urls = ['https://www.securityweek.com/virus-threats']

    def parse(self, response):
        topics = []
        for sel in response.xpath('//*[@id="category-page"]/div/div/div[5]/div/div/div[2]/div[*]/div/span/a'):
            topic = {'title': sel.xpath('text()').extract()[0], 'link': "https://www.securityweek.com"+sel.xpath('@href').extract()[0], 'src': response.request.url}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecEnNewsItem()
        item['title'] = topic['title']
        item['content'] = "".join(selector.xpath('//*[@class="node clear-block"]/div[2]/p[*]/span/span/text()').extract())
        item['uri'] = topic['link']
        item['src'] = topic['src']
        print('Finish scan title:' + item['title'])
        yield item


import scrapy
from scrapy import Request, Selector

from sec_news_en_scrapy.items import SecEnNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "securityaffairs"
    allowed_domains = ["securityaffairs.co"]
    start_urls = ['http://securityaffairs.co/wordpress/category/security']

    def parse(self, response):
        topics = []
        for sel in response.xpath('//*[@class="post_header_wrapper"]/div[*]//h3/a'):
            topic = {'title': sel.xpath('text()').extract()[0], 'link': sel.xpath('@href').extract()[0], 'src': response.request.url}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecEnNewsItem()
        item['title'] = topic['title']
        item['content'] = "".join(selector.xpath('//*[@id="content_wrapper"]/div/div/div[1]/div[3]/div[1]/div[1]/div/p/text()').extract())
        item['uri'] = topic['link']
        item['src'] = topic['src']
        print('Finish scan title:' + item['title'])
        yield item


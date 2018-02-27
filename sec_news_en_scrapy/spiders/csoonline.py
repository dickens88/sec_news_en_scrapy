import scrapy
from scrapy import Request, Selector

from sec_news_en_scrapy.items import SecEnNewsItem


class SecNewsSpider(scrapy.Spider):
    name = "csoonline"
    allowed_domains = ["csoonline.com"]
    start_urls = ['https://www.csoonline.com/category/hacking/']

    def parse(self, response):
        topics = []
        prefix = "https://www.csoonline.com"
        for sel in response.xpath('//*[@id="page-wrapper"]/section/section[@class="bodee"]/div[@class="main-col"]/div[@class="river-well article"]/div/h3/a'):
            topic = {'title': sel.xpath('text()').extract(), 'link': prefix + sel.xpath('@href').extract()[0], 'src': response.request.url}
            topics.append(topic)

        for topic in topics:
            yield Request(url=topic['link'], meta={'topic': topic}, dont_filter=False, callback=self.parse_page)

    def parse_page(self, response):
        topic = response.meta['topic']
        selector = Selector(response)

        item = SecEnNewsItem()
        item['title'] = topic['title'][0]
        item['content'] = "".join(selector.xpath('//*[@id="drr-container"]/p[*]/text()').extract())
        item['uri'] = topic['link']
        item['src'] = topic['src']
        print('Finish scan title:' + item['title'])
        yield item






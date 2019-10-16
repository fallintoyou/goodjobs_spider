import scrapy
from goodjobs.items import GoodjobsItem

class Goodjobs(scrapy.spiders.Spider):
    name = "goodjobs"
    allowed_domains = ["goodjobs.cn"]
    base_url = 'https://search.goodjobs.cn'
    start_urls = [
        "https://search.goodjobs.cn/index.php?keyword=php&boxwp=c1043"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="SearchJobList"]'):
            jobname = sel.xpath('ul//a/@title').extract()
            item = GoodjobsItem()
            item['jobname'] = jobname
            yield item

        next_page_url = self.base_url + response.xpath('//div[@class="p_in"]//a[contains(text(),"下一页")]/@href').extract()[0]
        yield scrapy.Request(next_page_url,callback=self.parse)
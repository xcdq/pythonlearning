import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/', 'https://xcdqaaa.blog.csdn.net/']

    def parse(self, response):
        print(self, response)
        pass

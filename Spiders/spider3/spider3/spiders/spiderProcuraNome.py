import scrapy


class SpiderprocuranomeSpider(scrapy.Spider):
    name = 'spiderProcuraNome'
    allowed_domains = ['www.cebraspe.org.br']
    start_urls = ['http://www.cebraspe.org.br/']

    def parse(self, response):
        pass

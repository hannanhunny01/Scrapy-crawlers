import scrapy
from scrapy_splash import SplashRequest


class SpiderlinkhrefSpider(scrapy.Spider):
    name = 'spiderLinkHref'
    allowed_domains = ['www.cebraspe.org.br']
    start_urls = ['http://www.cebraspe.org.br/']

    script ='''
    function main(splash, args)
    assert(splash:go(args.url))
    assert(splash:wait(10))
    return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
    
    '''
    def start_requests(self):
      url ='https://www.cebraspe.org.br/pas/subprogramas/2019_2021/3'
      yield SplashRequest(url=url,callback=self.parse,endpoint="execute",args={'lua_source':self.script})


    def parse(self, response):
      print(response.body)

      #links = response.xpath('//a[contains(@href,"PAS_21/Consulta")]/@href').getall()
      hrefs = response.xpath('//a[contains(@href,"https")]/@href').getall()
      #print(links)
      print(hrefs)
     # for href in links:
      #  yield{
       #   'link': href.xpath('//a[contains(@href,"PAS_21/Consulta")]/@href').get()
        #}
      
      

        #a= response.body
        #b=a.xpath('//a[contains(@href,"PAS_21/Consulta")]/@href').getall
        #print(b)
    #  for link in links:
     #   yield{
      #    'link':link

     #   }
      count =0
      for href in hrefs:
        
        yield{
          '_id':count,
          'href':href

        }
        count= count+1
      
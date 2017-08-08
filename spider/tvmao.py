###scrapy爬取tvmao上的剧情，只取第一个
from scrapy.spider import Spider  
from scrapy.selector import Selector  
  
from tutorial.items import DmozItem  
  
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["tvmao.com"]  
    start_urls = [  
         "http://www.tvmao.com/drama/L2gvKSE=/episode/1"  
    ]
    
    def parse(self, response):    
        filename='aaa'
        bbb='abc'
        ccc=response.xpath('//article//p/text()').extract()[1].encode('utf-8')
        with open(filename,'wb') as f:
           # f.write(sel.xpath('//title/text()').extract())
           #print ccc
           f.write(str(ccc))

###scrapy通过for in爬取所有p剧情
from scrapy.spider import Spider  
from scrapy.selector import Selector  
  
from tutorial.items import DmozItem  
  
class DmozSpider(Spider):  
    name = "dmoz"  
    allowed_domains = ["tvmao.com"]  
    start_urls = [  
         "http://www.tvmao.com/drama/L2gvKSE=/episode/1"  
    ]
    
    def parse(self, response):    
        filename='aaa'

        text=''
        ccc=response.xpath('//article//p/text()').extract()
        for i in ccc:
            text=text+i.encode('utf-8')+"\r\n"

        with open(filename,'wb') as f:
           f.write(text)






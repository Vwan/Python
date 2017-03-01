from scrapy.spiders import Spider
from scrapy.selector import Selector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(Spider):
    name="craig"
    allowed_domains=["fang.com"]
    start_urls=["http://fangjia.fang.com/process/yt/2416678441_%ba%a3%d0%c5%bb%db%d4%b0%ce%f7%c7%f8.htm"]

    def parse(self,response):
        hxs=Selector(response)
        titles=hxs.xpath("//div[@class='neighborbox-table']/table/tbody")
        items=[]
        for title in titles:
            
            item=CraigslistSampleItem()
            item["title"]=title.xpath("/tr/th/text()").extract()
            item["link"]=title.xpath("/tr/td/text()").extract()
            print "test--------------------"
           # print "********title is:********" + item["title"],"\n------link is: ------"+item["link"]
            items.append(item)
            return items

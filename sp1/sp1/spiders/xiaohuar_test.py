# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http import Request

class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar_test'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']

    def parse(self, response):
        # 要废弃
        # hxs = HtmlXPathSelector(response)
        # print(hxs)
        # result = hxs.select('//a[@class="item_list"]')

        hxs = Selector(response=response)
       
        #result = hxs.select("//div[@class=xxx/@href").extract()#后面这个函数可以将其变成列表
        #result = hxs.select("//div[@class=xxx]/text()").extract()
        user_list = hxs.xpath('//div[@class="itme masonry_brick"]')
        # #然后对每个进行循环
        
        for item in user_list:
            price = item.xpath('.//span[@class="price"]/text()').extract_first()
        #   #上面的意思是"itme masonry"的下一级目录找，即总目录的子子孙孙。 最后一个函数的意思是取第一个
        # #     print(price)
            url = item.xpath('div[@class="item_t"]/div[@class="title"]//a/@href').extract_first()
        #   #上面的意思是，首先是儿子，然后/div是在儿子目录找，然后//a是在子孙找
            #print(price.url)

        #接下来拿其他页的内容
        result = hxs.xpath('//a[re:test(@href,"http://www.xiaohuar.com/list-1-\d+.html")]/@href')
        
        #假设下面已经出来两个网页
        #result = ["xxxxx","yyyyy"]
        #开始循环，将以下任务重新放入调度器里
        for url in result:
            yield Request(url=url,callback=self.parse)#上面函数名就是parse，这样就可以源源不断发请求

        #为了防止重复爬取某一页面，要进行去重
        #自定义去重规则：写一个类，然后在配置文件中指定    
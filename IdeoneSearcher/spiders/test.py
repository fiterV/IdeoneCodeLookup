import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from termcolor import colored
from urllib.parse import urljoin
from IdeoneSearcher.items import IdeonesearcherItem
import re
from termcolor import colored
from scrapy.exceptions import CloseSpider
import urllib

DEBUG = True

def Debug():
    for i in range(10):
        print(colored(
            '-----------------------------------------------------------------------------------------------> Look over here, boy',
            color='red'))

def writeHTMLToLogFile(sel):
    with open('log.html', 'w') as f:
        print(sel.xpath('//html').extract(), file=f)

class IdeoneSpider(Spider):
    name='ideone'
    allowed_domains = ['ideone.com']
    start_urls = ['http://ideone.com/recent/']

    #link to paste provided in link is like this http://ideone.com/<code>
    #we need to transform it into http://ideone.com/plain/<code>
    def getProgramCode(self, link):
        link=link.replace('.com/', '.com/plain/')
        return urllib.request.urlopen(link).read().decode('utf-8')

    def getNext(self, link):
        le = len(link) - 1
        next = ""
        while (link[le].isdigit() == True):
            next += link[le]
            le -= 1
        next = next[::-1]
        if (next==""):
        	next="0"
        next = str(int(next) + 1);
        next = urljoin('http://ideone.com/recent/', next)
        return next

    def pasteParse(self, response):
        sel = Selector(response)
        #writeHTMLToLogFile(sel)
        #Debug()
        print(response.url)
        code=self.getProgramCode(response.url)
        occs=re.search('bits', code)
        if occs is not None:
            #with open('result.json', 'a') as f:
            #    print(response.url, file=f)

            l = ItemLoader(item=IdeonesearcherItem(), response=response)
            l.add_value('url', str(response.url))
            yield l.load_item()



    def parse(self, response):
        sel = Selector(response)
        links = [urljoin('http://ideone.com', i) for i in sel.xpath('//strong/a/@href').extract()]


        for paste in links:
            yield scrapy.Request(url=paste, callback=self.pasteParse)
        # next = self.getNext(response.url)
        # if next=='http://ideone.com/recent/3':
        # 	raise CloseSpider("Enough for this minute")
        # print(colored('<---------------- {} ------------------------->'.format(next), color='green'))
        #
        # yield scrapy.Request(url=next, callback=self.parse)



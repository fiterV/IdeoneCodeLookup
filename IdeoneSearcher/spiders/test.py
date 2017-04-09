import scrapy
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from IdeoneSearcher.items import IdeonesearcherItem
from scrapy.exceptions import CloseSpider
import re
from termcolor import colored
import urllib
from urllib.parse import urljoin
from xml.etree import ElementTree
import datetime

DEBUG = True
DATE_FORMAT='%H-%m-%S %d %B %Y'

def Debug():
    for i in range(10):
        print(colored(
            '-----------------------------------------------------------------------------------------------> Look over here',
            color='red'))

def writeHTMLToLogFile(sel):
    with open('log.html', 'w') as f:
        print(sel.xpath('//html').extract(), file=f)

class IdeoneSpider(Spider):
    name='ideone'
    allowed_domains = ['ideone.com']
    start_urls = ['http://ideone.com/recent/']

    def __init__(self):
        dom = ElementTree.parse('../../settings.conf')
        self.regExpForCode=dom.find('substring').text
        self.lastUrl = dom.find('lastUrl').text
        print(self.lastUrl)


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
        code=self.getProgramCode(response.url)
        occs=re.search(self.regExpForCode, code)
        if occs is not None:
            l = ItemLoader(item=IdeonesearcherItem(), response=response)
            l.add_value('url', str(response.url))
            l.add_value('scrapedOn', datetime.datetime.now().strftime(DATE_FORMAT))
            yield l.load_item()

    def parse(self, response):
        sel = Selector(response)
        links = [urljoin('http://ideone.com', i) for i in sel.xpath('//strong/a/@href').extract()]


        for paste in links:
            yield scrapy.Request(url=paste, callback=self.pasteParse)
        next = self.getNext(response.url)
        if next==self.lastUrl:
        	raise CloseSpider("We've got to the last url")
        print(colored('<---------------- {} ------------------------->'.format(next), color='green'))

        yield scrapy.Request(url=next, callback=self.parse)



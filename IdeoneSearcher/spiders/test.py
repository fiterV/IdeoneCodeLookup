import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from IdeoneSearcher.items import IdeonesearcherItem
from scrapy.exceptions import CloseSpider
import re
from termcolor import colored
import urllib
from urllib.parse import urljoin
import datetime
from configparser import ConfigParser

DEBUG = True
DATE_FORMAT='%H-%m-%S %d %B %Y'

def Debug():
    for i in range(10):
        print(colored(
            '-----------------------------------------------------------------------------------------------> Look over here',
            color='red'))

class IdeoneSpider(Spider):
    name='ideone'
    allowed_domains = ['ideone.com']
    start_urls = ['http://ideone.com/recent/']

    def __init__(self):
        config = ConfigParser()
        config.read('settings.conf')
        self.regExpForCode=config['IdeoneCodeLookupConfig']['RegExp']
        self.lastUrl = config['IdeoneCodeLookupConfig']['lastUrl']


    #link to paste provided in link is like this http://ideone.com/<code>
    #we need to transform it into http://ideone.com/plain/<code>
    def getProgramCode(self, link):
        link=link.replace('.com/', '.com/plain/')
        return urllib.request.urlopen(link).read().decode('utf-8')

    #link example http://ideone.com/recent/<number of the Page>
    def getNextLink(self, link):
        #firstly we will take the number at the end of a string
        #the simplest way - Regex
        match = re.search('\d+', link)
        if match is None:
            next=0
        else:
            next = int(match.group())
        next+=1
        next = 'http://ideone.com/recent/{}'.format(next)
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
        links = [urljoin('http://ideone.com', i) for i in sel.xpath('//strong/a/@href').extract() if (i.find('recent')==-1)]

        for paste in links:
            yield scrapy.Request(url=paste, callback=self.pasteParse)
        next = self.getNextLink(response.url)
        if next!=self.lastUrl:
            print(colored('<---------------- {} ------------------------->'.format(next), color='green'))
            yield scrapy.Request(url=next, callback=self.parse)



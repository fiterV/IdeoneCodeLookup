#!/usr/bin/python3
import os
import argparse
import configparser
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

os.chdir('/bin/ideone')
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--regexp', help='Regular expression for the substring in the code')
parser.add_argument('-c', '--count', help='Amount of pages that you want to scrape')
args = parser.parse_args()

args.count='http://ideone.com/recent/'+args.count

conp = configparser.ConfigParser()
conp.read('settings.conf')
conp['IdeoneCodeLookupConfig']['RegExp']=args.regexp
conp['IdeoneCodeLookupConfig']['lasturl']=args.count

with open('settings.conf', 'w') as f:
	conp.write(f)
#os.system('scrapy crawl ideone --loglevel ERROR')


sett = get_project_settings()
sett['LOG_LEVEL']='ERROR'
process = CrawlerProcess(sett)

process.crawl('ideone')
process.start()
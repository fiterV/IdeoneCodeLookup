#IdeoneCodeLookup

##Overview
A script, that let you find the code on [Ideone](https://ideone.com) substring of which matches some [RegExp](https://en.wikipedia.org/wiki/Regular_expression)

##How to use

**settings.conf**-configurations for the script.
Example of the file:
`
[IdeoneCodeLookupConfig]
RegExp=924844033
lastUrl=http://ideone.com/recent/5
`
To execute the program: `scrapy crawl ideone`
You can store result to [JSON](https://en.wikipedia.org/wiki/JSON) or [CSV](https://en.wikipedia.org/wiki/Comma-separated_values):
`scrapy crawl ideone -t json -o res.json`
`scrapy crawl ideone -t csv -o res.csv`
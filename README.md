# IdeoneCodeLookup

## Overview
A script, that let you find the code on [Ideone](https://ideone.com) substring of which matches some [RegExp](https://en.wikipedia.org/wiki/Regular_expression)

## Configuration

**settings.conf**-script main settings.<br>

`[IdeoneCodeLookupConfig]`<br>
`RegExp=bits`<br/>
`lastUrl=http://ideone.com/recent/5`<br/>
That basically means that we're going to scrape all codes to **.../recent/5** and select only ones that have **bits** substring in them

## Usage 
To execute the program: 

`scrapy crawl ideone`

You can store result to [JSON](https://en.wikipedia.org/wiki/JSON) or [CSV](https://en.wikipedia.org/wiki/Comma-separated_values):

`scrapy crawl ideone -t json -o res.json`

`scrapy crawl ideone -t csv -o res.csv`
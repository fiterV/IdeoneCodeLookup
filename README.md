# IdeoneCodeLookup

## Overview
A script, that let you find the code on [Ideone](https://ideone.com) substring of which matches some [RegExp](https://en.wikipedia.org/wiki/Regular_expression)

## How to use

**settings.conf**-script main settings.<br>
Example of the file:

`[IdeoneCodeLookupConfig]`<br>
`RegExp=924844033`<br/>
`lastUrl=http://ideone.com/recent/5`<br/>

To execute the program: 

`scrapy crawl ideone`

You can store result to [JSON](https://en.wikipedia.org/wiki/JSON) or [CSV](https://en.wikipedia.org/wiki/Comma-separated_values):

`scrapy crawl ideone -t json -o res.json`

`scrapy crawl ideone -t csv -o res.csv`
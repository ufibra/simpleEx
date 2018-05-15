# simpleEx
Basic scrapy project as an example...

XPath usage:

- run: scrapy shell https://SOMEURL/

- run: div = response.xpath('copy a xpath on browser')

- then you run: div.extract()

Running spiders scripts:

- run: scrapy crawl 'spidername'

Save into a json file:

- run: scrapy crawl 'spidername' -o spidername.json

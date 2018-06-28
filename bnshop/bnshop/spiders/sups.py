# -*- coding: utf-8 -*-
import scrapy


class SupsSpider(scrapy.Spider):
    name = 'sups'
    #allowed_domains = ['https://loja.boldnutrition.com.br/']
    start_urls = ['https://loja.boldnutrition.com.br/']

    def parse(self, response):
        results = response.css('.product-grid .item')
        name = scrapy.Field()
        price = scrapy.Field()
        for result in results:
            name = result.css('.product-item_name ::text').extract_first()
            price = result.css('.item-price ::text').extract_first()
            yield {
                'name': name,
                'price': price
            }

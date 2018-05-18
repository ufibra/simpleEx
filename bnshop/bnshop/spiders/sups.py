# -*- coding: utf-8 -*-
import scrapy


class SupsSpider(scrapy.Spider):
    name = 'sups'
    #allowed_domains = ['https://loja.boldnutrition.com.br/']
    start_urls = ['https://loja.boldnutrition.com.br/']

    def parse(self, response):
        results = response.xpath("//*[contains(@id, 'price_display')]/text()")
        for result in results:
            print result.extract()
# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/ir-root/ir-content/ir-course-catalog/section/div/div/div/div/div")
        for div in divs:
            link = div.xpath('.//h3/a')
            href = link.xpath('./@href').extract_first()
            # yield is a parcial and gradual return
            yield scrapy.Request(
                url = 'https://br.udacity.com%s' % href,
                callback = self.parse_detail
            )

    def parse_detail(self, response):
        pass

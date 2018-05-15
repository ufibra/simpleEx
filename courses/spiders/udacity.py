# -*- coding: utf-8 -*-
import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    start_urls = ['https://br.udacity.com/courses/all/']

    def parse(self, response):
        divs = response.xpath("/html/body/ir-root/ir-content/ir-course-catalog/section/div/div/div/div/div")
        for div in divs:
            link = div.xpath('.//h3/a')
            title = link.xpath('./text()').extract_first()
            href = link.xpath('./@href').extract_first()
            # we want the img that contains className img-responsive
            img = div.xpath('.//img[contains(@class, "img-responsive")]/@src').extract_first()
            description = div.xpath('.//div[2]/div[2]/text()').extract_first()
            # yield is a parcial and gradual return
            yield {
                'title': title,
                'url': href,
                'image': img,
                'description': description
            }
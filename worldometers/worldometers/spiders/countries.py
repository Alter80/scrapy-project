# -*- coding: utf-8 -*-
import scrapy
import logging

from scrapy.http import request

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #title = response.xpath("//h1/text()").get() #usual method for persing h1
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()     #. or period use korte hobe jokhon kono selector object thakbe. but jodi response object thake etar maybe dorkar porbe na. 
            link = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info{link}"

            #Alternative method
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url= absolute_url)

            #3rd method
            # yield response.follow(url= link)

            # yield{                      #jehetu for loop so yield ta for loop er vitore hobe naile 1 country name show kore loop exit hobe.
            #     'country_name': name,
            #     'country_link': link
            # }

            yield response.follow(url= link, callback = self.parse_country, meta = {'country_name' : name})


    def parse_country(self, response):
        #logging.info(response.url)
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr") #always use single quote in xpath class define
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield {
                'country_name': name,
                'year': year,
                'population': population
            }


#first spyder build        

# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #title = response.xpath("//h1/text()").get() #usual method for persing h1
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()     #. or period use korte hobe jokhon kono selector object thakbe. but jodi response object thake etar maybe dorkar porbe na. 
            link = country.xpath(".//@href").get()

            yield{                      #jehetu for loop so yield ta for loop er vitore hobe naile 1 country name show kore loop exit hobe.
                'country_name': name,
                'country_link': link
            }

#first spyder build        

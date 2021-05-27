import scrapy


class PricelistSpider(scrapy.Spider):
    name = 'pricelist'
    allowed_domains = ['www.glassesshop.com']
    # start_urls = ['https://www.glassesshop.com/bestsellers']

    def start_requests(self):
        yield scrapy.Request(url= 'https://www.glassesshop.com/bestsellers', callback= self.parse, headers={
            'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36'
        })

    def parse(self, response):
        for product in response.xpath("//div[@id='product-lists']/div"):
            yield{
                'url' : product.xpath(".//div[@class='p-title']/a/@href").get(),
                'image_url' : product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@data-src").get(),
                'name' : product.xpath("normalize-space(.//div[@class = 'p-title']/a/text())").get(),
                'price' : product.xpath(".//div[@class = 'p-price']/div/span/text()").get(),
                #'User-Agent' : response.request.headers['User-Agent']

            }

        next_page = response.xpath("//li[@class= 'page-item']/a[text() = 'Next']/@href").get()

        if next_page:
            yield scrapy.Request(url= next_page, callback= self.parse, headers={
                'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36'
            })


    
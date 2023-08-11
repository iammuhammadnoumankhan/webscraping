import scrapy
from chocolatescraper.items import ChocolateProduct
from chocolatescraper.itemloaders import ChocolateProductLoader
# from chocolatescraper.pipelines import SavingToMySQLPipline, DuplicatesPipline

class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://www.chocolate.co.uk/collections/all"]

    def parse(self, response):
        
        products = response.css('product-item')

        # protuct_item = ChocolateProduct()
        for product in products:

            cholocate = ChocolateProductLoader(item=ChocolateProduct(), selector= product)
            cholocate.add_css('name', 'a.product-item-meta__title::text'),
            cholocate.add_css('price', 'span.price', re = '<span class="price">\n              <span class="visually-hidden">Sale price</span>(.*)</span>'),
            cholocate.add_css('url' ,'div.product-item-meta a::attr(href)') 
            yield cholocate.load_item()

            # yield{
            #     'name' : product.css('a.product-item-meta__title::text').get(),
            #     'price' : product.css('span.price').get().replace('<span class="price">\n              <span class="visually-hidden">Sale price</span>','').replace('</span>',''),
            #     'url' : product.css('div.product-item-meta a').attrib['href']
            # }

        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page is not None:
            next_page_url = "https://www.chocolate.co.uk" + next_page
            yield response.follow(next_page, callback=self.parse)

    
        
        pass

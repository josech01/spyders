import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from .items import MetorappItem

class Spyder1Spider(scrapy.Spider):
    name = 'jose'
    item_count = 0
    allowed_domain = ['https://www.falabella.com.pe']
    start_urls = ['https://www.falabella.com.pe/falabella-pe/category/cat4100481/Hombre']
    rules = {
        # Para cada item
        Rule(LinkExtractor(allow=(), restrict_xpaths=(
            '//*[@id="fbra_browseProductList"]/div/div/section[2]/div[3]/div/div[2]/div[3]/div/span'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[@id="fb-pod__item--880600744"]/div[2]/a[@class="fb-pod__header-link gridSize-1"]')),
             callback='parse_item', follow=False)
    }
    
    def parse_item(self, response):
        ml_item = MetorappItem()
        # info de producto
       'titulo': response.css('h1.fb-product-cta__title::text').extract_first(),
            'codigo': response.css('p.fb-product-sets__product-code::text').extract_first(),
            'imagen': response.xpath('//*[@id="js-fb-pp-photo__media"]/@src').extract_first(),
            'color':  response.xpath('//*[@id="fbra_browseMainProduct"]/div/div/div[2]/div/div[4]/div[2]/div/div/div[1]/ul/li/label').extract_first(),
            'tamaños': response.xpath('//li[@class="fb-inline-dropdown__list-item"]/a/text()').extract_first()
            'precio': quote.css(' small.author::text').extract_first(),
            'tags': quote.css('div.tags a.tag::text').extract(),
        # ml_item['platforms'] = response.xpath('normalize-space(//div[@class="playable-on__button-set"]/a)').extract_first()

        next_page = response.xpath('//*[@id="fbra_browseProductList"]/div/div/section[2]/div[3]/div/div[2]/div[3]/div/span').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
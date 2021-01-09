import scrapy 
from ..items import BbctestItem
class quaotspider(scrapy.Spider):
    name='bbcteest'
    start_urls=['https://www.bbc.com/']
    
    def parse(self,response):
        items=BbctestItem()
        atricle_head=response.css('a.block-link__overlay-link')
        atricle_text=response.css('p.media__summary')
        for article,body  in zip(atricle_head,atricle_text):
            headline=article.css('::text').extract_first()
            link=article.css('::attr(href)').extract_first()
            text=body.css('::text').extract_first()
            items['headline']=headline
            items['link']=link
            items['text']=text
            yield items
            
import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy.exceptions import CloseSpider
from demo.items import DemoItem


class TiempoSpider(scrapy.Spider):
    name = 'tiempo'
    start_urls = [
        'https://www.eltiempo.com/justicia/paz-y-derechos-humanos/falsos-positivos-de-soacha-ministro-de-defensa-ivan-velasquez-pidio-perdon-812315']


    def parse(self, response):
        mis_items = DemoItem()
        mis_items['titulo'] = response.xpath('//div[@class="titulo-principal-bk"]/h1/text()').get()
        mis_items['articulo'] = response.xpath('//p[@class="contenido"][2]/text()').get()

        yield mis_items

# {
#  'titulo': 'Falsos positivos de Soacha: 15 años después, Estado pide perdón a '
#            'familias de víctimas',
# 
#  'articulo': 'Fueron 19 las familias de víctimas de Bogotá y Soacha las que '
#              'escucharon el mensaje del ministro de la Defensa en la tarde de '
#              'este martes. Aunque recibieron su pedido de perdón,',
# }
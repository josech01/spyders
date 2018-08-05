# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MetorappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    tamaños = scrapy.Field()
    color = scrapy.Field()
    imagen = scrapy.Field()
    precio_internet = scrapy.Field()
    precio_normal = scrapy.Field()
    descuento = scrapy.Field()
    codigo = scrapy.Field()
    modelo = scrapy.Field()
    material = scrapy.Field()
    pass
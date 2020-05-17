# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from rozetka.models import Product, Category


class CategoryPipeline:
    def process_item(self, item, spider):
        # if isinstance(item, Category):
        #     item = Category.objects.create(name=item['name'], link=item['link'])
        item.save()
        return item


class ProductPipeline:
    def process_item(self, item, spider):
        # if isinstance(item, Product):
        #     item = Product.objects.create(name=item['name'], link=item['link'], link_to_photo=item['link_to_photo'],
        #                               old_price=item['old_price'], cheaper_price=item['cheaper_price'],
        #                               sale=item['sale'], sale_promo_date=item['sale_promo_date'],)
        #                               # category=Category.objects.get(link=item['category']))/
        item.save()
        return item

import scrapy

from shops_items.items import CategoryItem, ProductItem


class ItemsSpider(scrapy.Spider):

    name = 'rozetka_hrefs'
    start_urls = [
        'https://rozetka.com.ua/promo/laughday/',
    ]
    number_of_pages = 0

    # parse promo page and save all categories and link to them
    def parse(self, response):
        global file
        file = open('text.txt', 'w')
        categories = []
        for div in response.css("div.preloader-trigger"):

            name = div.css("span::text").getall()[2].strip()
            href_to_new_catalog = div.css("a::attr(href)").get()
            file.write(name + ' --- ' + href_to_new_catalog + "\n")

            iCategory = CategoryItem()
            iCategory['name'] = name
            iCategory['link'] = href_to_new_catalog


            categories.append(iCategory)

            # for each category parse count of products pages
            for category in categories:
                href_to_new_catalog = category['link']
                yield scrapy.Request(href_to_new_catalog, meta={'category_item': category},
                                     callback=self.parse_count_of_page_for_category)

    def parse_count_of_page_for_category(self, response):
        item = response.meta['category_item']
        count_pages = int(response.css("ul.paginator-catalog li span::text").getall()[-1])
        page = 0
        links = []
        count_pages = 1
        # for each category create list links that will parse to search products
        while count_pages != 0:
            count_pages -= 1
            page += 1
            href_to_new_catalog_page = item['link'] + "&p={number_of_page}".format(number_of_page=page)
            links.append(href_to_new_catalog_page)

        # loop for category` links
        for link in links:
            href_to_new_catalog_page = link
            yield scrapy.Request(href_to_new_catalog_page, self.parse_items_on_new_page)

    def parse_items_on_new_page(self, response):
        promo_date = response.css("div.rz-promopage-promocode span::text").get().strip().split(" ")[-1]
        promo_date = self.formatDate(promo_date)
        for item in response.css("div.g-i-tile-catalog"):

            name = item.css('a.novisited::text').get().strip().split("(")[0]

            href_to_file = item.css('a.novisited::attr(href)').get()

            link_to_photo = item.css('div.g-i-tile-i-image img::attr(data-rz-lazy-load-src)').get()

            old_price_list = item.css('div.g-price-old-uah::text')
            old_price = self.isNone(old_price_list)

            cheaper_price_list = item.css('div.g-price-uah::text')
            cheaper_price = self.isNone(cheaper_price_list)

            sale_promo_date = promo_date

            if name != "" and href_to_file != "#":
                file.write(name + " " + href_to_file + "\n")

            iProduct = ProductItem()
            iProduct['name'] = name
            iProduct['link'] = href_to_file
            iProduct['link_to_photo'] = link_to_photo
            iProduct['old_price'] = old_price
            iProduct['cheaper_price'] = cheaper_price
            iProduct['sale'] = 100 - (cheaper_price * 100)/old_price
            iProduct['sale_promo_date'] = sale_promo_date
            yield iProduct

    def isNone(self, lists):
        if lists is None:
            price = 0
        else:
            lists = lists.get().strip().split(" ")
            price = ""
            price = int(price.join(lists))
            print(price)

        return price

    def formatDate(self, date):
        list_date = date.split('.')[::-1]
        new_date = "-"
        new_date = new_date.join(list_date)
        print(new_date)

        return new_date

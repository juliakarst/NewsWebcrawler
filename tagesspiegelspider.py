# -*- coding: utf-8 -*-
import scrapy



class TSpider(scrapy.Spider):
    """Diese Klasse scrapt die Themenseite "China" von tagesspiegel.de """

    # es wird nur der Themenschwerpunkt gescrapt, bei Scrapen aller Artikel kann um weitere Kategorien ergänzt werden
    category = {"ThemaChina": {"https://www.tagesspiegel.de/themen/china/"},
                }

    selected_categories = []
    existing_urls = []

    # initalisere den Spider
    def __init__(self, cat_list=['ThemaChina'], *args, **kwargs):
        super(TSpider, self).__init__(*args, **kwargs)
        for c in cat_list:
            if c in self.category:
                for url in self.category[c]:
                    self.start_urls.append(url)



    name = "tagesspiegel"
    start_urls = []

    def parse(self, response):
        """in parse werden die URLS der einzelnen Artikel und der nächsten Seite ausgelesen"""

        # die URL für die nächste Seite
        next_page = response.xpath("//li[contains(@class, 'hcf-paging-forward')]/a/@href").get()

        # die URLs für die ersten Artikel (urls1) und für die weiteren Artikel (urls2)
        urls1 = response.xpath("//li[contains(@class, 'hcf-teaser hcf-left')]/h2/a/@href").getall()
        urls2 = response.xpath("//div[contains(@class, 'hcf-media-wrapper')]/a/@href").getall()
        urls = urls1+urls2

        # folge den URls und füge sie den exiting_urls bei
        for url in urls:
            if url not in self.existing_urls:
                self.existing_urls.append(url)
                yield response.follow(url, self.parse_article)

        # folge dem Link zur nächsten Seite
        if next_page is not None:
            #print("next page: "+ next_page)
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        """in parse_article werden die Informationen der Artikel ausgelesen"""

        # Überprüfe, ob es sich um Premium-Artikel handelt
        premium = response.xpath("//div[contains(@class, 'Sc9 Faq')]/span/text()").get()

        # sämtliche Paragraphen des Artikels
        body = response.xpath("//div[contains(@class, 'ts-article-body')]/p/text()").getall()
        # alternativen zu Body, da nicht alle Artikel dieselbe Struktur haben
        body_textrun = response.xpath("//p/span[contains(@class, 'TextRun')]/text()").getall()
        body_inspan = response.xpath("//div[contains(@class, 'ts-article-body')]/p/span/text()").getall()
        # verlinkte Wörter
        bodylinked = response.xpath("//p/a/text()").getall()

        if not premium:
            try:
                overline = response.xpath("//span[contains(@class, 'ts-overline')]/text()").get()
                headline = response.xpath("//span[contains(@class, 'ts-headline')]/text()").get()
                title = overline+". "+headline
            except:
                title = "no_headline"


            try:
                author = response.xpath("//span[contains(@class, 'ts-author')]/a/text()").get()
                if not author:
                    author = "no_author"
            except:
                author = "no_author"

            try:
                date_published = response.xpath("//div[contains(@class, 'ts-meta')]/time/text()").get()
            except:
                date_published = "no_date"

            body_str = ""
            for p in body:
                if not body_str:
                    body_str += p
                else:
                    body_str = body_str + " " + p
            for l in bodylinked:
                if not body_str:
                    body_str += l
                else:
                    body_str = body_str + " " + l
            for t in body_textrun:
                if not body_str:
                    body_str += t
                else:
                    body_str = body_str + " " + t
            for s in body_inspan:
                if not body_str:
                    body_str += s
                else:
                    body_str = body_str + " " + s

            item = {}
            item["title"] = title
            item["author"] = author
            item["date_published"] = date_published
            item["url"] = response.url
            item["article_text"] = body_str
            item["source"] = "tagesspiegel"

            yield item


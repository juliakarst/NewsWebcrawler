# -*- coding: utf-8 -*-
import scrapy
import json


class WiWoSearchSpider(scrapy.Spider):
    """Diese Klasse scrapt wiwo.de mit Suchbegriff "China" und Filter "Artikel"""

    # für den Zeitraum ab 2020 werden nur die ersten 400 Seiten benötigt
    # es wurde in einzelne Abschnitte von je 25 Seiten aufgesplittet um nicht zu viele Anfragen an die Webseite zu stellen
    category = {"til25": {"https://www.wiwo.de/suche/?p19868864=1&sw=china&search-period=&article=article"},
                "til50": {"https://www.wiwo.de/suche/?p19868864=25&sw=china&search-period=&article=article"},
                "til75": {"https://www.wiwo.de/suche/?p19868864=50&sw=china&search-period=&article=article"},
                "til100": {"https://www.wiwo.de/suche/?p19868864=75&sw=china&search-period=&article=article"},
                "til125": {"https://www.wiwo.de/suche/?p19868864=100&sw=china&search-period=&article=article"},
                "til150": {"https://www.wiwo.de/suche/?p19868864=125&sw=china&search-period=&article=article"},
                "til175": {"https://www.wiwo.de/suche/?p19868864=150&sw=china&search-period=&article=article"},
                "til200": {"https://www.wiwo.de/suche/?p19868864=175&sw=china&search-period=&article=article"},
                "til225": {"https://www.wiwo.de/suche/?p19868864=200&sw=china&search-period=&article=article"},
                "til250": {"https://www.wiwo.de/suche/?p19868864=225&sw=china&search-period=&article=article"},
                "til275": {"https://www.wiwo.de/suche/?p19868864=250&sw=china&search-period=&article=article"},
                "til300": {"https://www.wiwo.de/suche/?p19868864=275&sw=china&search-period=&article=article"},
                "til325": {"https://www.wiwo.de/suche/?p19868864=300&sw=china&search-period=&article=article"},
                "til350": {"https://www.wiwo.de/suche/?p19868864=325&sw=china&search-period=&article=article"},
                "til375": {"https://www.wiwo.de/suche/?p19868864=350&sw=china&search-period=&article=article"},
                "til400": {"https://www.wiwo.de/suche/?p19868864=375&sw=china&search-period=&article=article"},
                }

    selected_categories = []
    existing_urls = []

    #initalisere den Spider
    def __init__(self, cat_list=["til325"], *args, **kwargs):
        super(WiWoSearchSpider, self).__init__(*args, **kwargs)
        for c in cat_list:
            if c in self.category:
                for url in self.category[c]:
                    self.start_urls.append(url)



    name = "wiwosearch"
    start_urls = []

    def parse(self, response):
        """in parse werden die URLS der einzelnen Artikel und der nächsten Seite ausgelesen"""

        # die URL für die nächste Seite
        next_page = response.xpath("//div[contains(@class, 'u-flex__item u-flex__item--right u-flex__item--center u-flex__item--basis25')]/a/@href").get()

        # die URLs der einzelnen Artikel
        allurls = response.xpath("//div[contains(@class, 'u-flex__item u-lastchild')]/a/@href").getall()
        # Premium-Artikel werden bereits hier aussortiert um unnötige Anfragen zu vermeiden
        premiumurls = response.xpath("//div[contains(@tt-premium, 'true')]/div/a/@href").getall()
        urls = list(set(allurls) ^ set(premiumurls))

        # folge den URls und füge sie den exiting_urls bei
        for url in urls:
            if url not in self.existing_urls:
                self.existing_urls.append(url)
                yield response.follow(url, self.parse_article)

        #folge dem Link zur nächsten Seite bis die Abbruchbedingung erreicht ist
        if next_page is not None:
            # Definiere die jeweilige Abbruchbedingung
            if "p19868864=325" in next_page:
                next_page = None
            else:
                print("next page: " + next_page)
                yield response.follow(next_page, self.parse)




    def parse_article(self, response):
        """in parse_article werden die Informationen der Artikel ausgelesen"""

        # Überprüfe, ob es sich um Premium-Artikel handelt
        premium = response.xpath("//article[contains(@class, 'isPremium')]/text()").get()

        #sämtliche Paragraphen des Artikels
        body = response.xpath("//div[contains(@class, 'u-richtext')]/p/text()").getall()

        bodylinked = response.xpath("//div[contains(@class, 'u-richtext')]/p/a/text()").getall()

        #besteht der Artikel aus mehreren Seiten, so soll dieser auf einer Seite gelesen werden
        one_page = response.xpath("//div[contains(@class, 'c-article-pagination__pages')]/a/@href").get()

        if not premium:
            if one_page:
                if one_page not in self.existing_urls:
                    yield response.follow(one_page, self.parse_article)
            else:

                try:
                    overline = response.xpath("//h2/span/text()").get()
                except:
                    overline = ""
                try:
                    headline = response.xpath("//h2/text()").get()
                except:
                    headline = ""

                if not overline:
                    if not headline:
                        title = "no_author"
                    else:
                        title = headline.replace("\n", " ")
                else:
                    if not headline:
                        title = overline.replace("\n", " ")
                    else:
                        title = (overline + ". " + headline).replace("\n", " ")

                author_str = ""
                try:
                    allauthors = response.xpath("//div[contains(@class, 'c-metadata u-margin-xl')]/div/a/span/text()").getall()
                    if type(allauthors) is list:
                        for a in allauthors:
                            if not author_str:
                                author_str += a
                            else:
                             author_str = author_str + ", " + a
                        author = author_str
                    if not allauthors:
                        author = "no_author"
                except:
                    author = "no_author"



                try:
                    date_published = response.xpath(
                        "//div[contains(@class, 'c-metadata u-margin-xl')]/time/text()").get()

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


                item = {}
                item["title"] = title
                item["author"] = author
                item["date_published"] = date_published
                item["url"] = response.url
                item["article_text"] = body_str
                item["source"] = "wirtschaftswoche"

                yield item

# -*- coding: utf-8 -*-
import scrapy



class SDSpider(scrapy.Spider):
    """Diese Klasse scrapt die DPA-Artikel zum Suchbegriff "China" auf süddeutsche.de """

    # jede Kategorie entspricht einem Monat
    category = {"Jan22": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2022-01-01T00%3A00%2F2022-01-31T23%3A59&startDate=10.01.2022&endDate=19.01.2022"},
                "Dec21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2022-02-21T00%3A00%2F2022-02-21T23%3A59&startDate=01.12.2021&endDate=31.12.2021"},
                "Nov21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-12-01T00%3A00%2F2021-12-31T23%3A59&startDate=01.11.2021&endDate=30.11.2021"},
                "Oct21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-11-01T00%3A00%2F2021-11-30T23%3A59&startDate=01.10.2021&endDate=31.10.2021"},
                "Sep21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-11-01T00%3A00%2F2021-11-30T23%3A59&startDate=01.09.2021&endDate=30.09.2021"},
                "Aug21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.08.2021&endDate=31.08.2021"},
                "Jul21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.07.2021&endDate=31.07.2021"},
                "Jun21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.06.2021&endDate=30.06.2021"},
                "May21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.05.2021&endDate=31.05.2021"},
                "Apr21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.04.2021&endDate=30.04.2021"},
                "Mar21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.03.2021&endDate=31.03.2021"},
                "Feb21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.02.2021&endDate=28.02.2021"},
                "Jan21": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.01.2021&endDate=31.01.2021"},
                "Dec20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.12.2020&endDate=31.12.2020"},
                "Nov20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.11.2020&endDate=30.11.2020"},
                "Oct20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.10.2020&endDate=31.10.2020"},
                "Sep20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.09.2020&endDate=30.09.2020"},
                "Aug20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.08.2020&endDate=31.08.2020"},
                "Jul20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.07.2020&endDate=31.07.2020"},
                "Jun20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.06.2020&endDate=30.06.2020"},
                "May20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.05.2020&endDate=31.05.2020"},
                "Apr20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.04.2020&endDate=30.04.2020"},
                "Mar20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.03.2020&endDate=31.03.2020"},
                "Feb20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.02.2020&endDate=29.02.2020"},
                "Jan20": {"https://www.sueddeutsche.de/news?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2021-09-01T00%3A00%2F2021-09-30T23%3A59&startDate=01.01.2020&endDate=31.01.2020"},


                }

    selected_categories = []
    existing_urls = []

    # initialisere den Spider
    def __init__(self, cat_list=['Dec21'], *args, **kwargs):
        super(SDSpider, self).__init__(*args, **kwargs)
        for c in cat_list:
            if c in self.category:
                for url in self.category[c]:
                    self.start_urls.append(url)



    name = "sueddeutsche"
    start_urls = []

    def parse(self, response):
        """in parse werden die URLS der einzelnen Artikel und der nächsten Seite ausgelesen"""

        # die URL für die nächste Seite
        rel_next_page = response.xpath("//li[contains(@class, 'arrow next')]/a/@href").get()
        #Suffix muss auf Suchkriterium der jeweiligen Kategorie angepasst werden
        suffix = "?search=china&sort=date&all%5B%5D=dep&typ%5B%5D=article&sys%5B%5D=dpa&catdpa%5B%5D=alles&time=2022-02-21T00%3A00%2F2022-02-21T23%3A59&startDate=01.12.2021&endDate=31.12.2021"

        # die URLs der einzelnen Artikel
        urls = response.xpath("//div[contains(@class, 'entrylist__content')]/a/@href").getall()

        # folge den URls und füge sie den exiting_urls bei
        for url in urls:
            if url not in self.existing_urls:
                self.existing_urls.append(url)
                yield response.follow(url, self.parse_article)

        # folge dem Link zur nächsten Seite
        if rel_next_page is not None:
            next_page = rel_next_page + suffix
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        """in parse_article werden die Informationen der Artikel ausgelesen"""

        # Überprüfe, ob es sich um Premium-Artikel handelt
        free = False
        try:
            dpa_article = response.xpath("//p[contains(@class, 'css-1dqanco')]/text()").get()
        except:
            dpa_article = ""
        if "dpa" in dpa_article:
            free = True
        else:
            free = False

        # sämtliche Paragraphen des Artikels
        body = response.xpath("//p[contains(@class, 'css-13wylk3')]/text()").getall()
        # verlinkte Wörter im Artikel
        linkedwords = response.xpath("//p[contains(@class, 'css-13wylk3')]/a/text()").getall()

        if free:
            try:
                maintitle = response.xpath("//h2/span[contains(@class, 'css-1tm5due')]/text()").get()
                subtitle = response.xpath("//h2/span[contains(@class, 'css-odme1c')]/text()").get()
                title = maintitle+". "+subtitle
            except:
                title = "no_headline"


            try:
                date_published = response.xpath("//div[contains(@class, 'css-1kfzr40')]/time/@datetime").get()
            except:
                date_published = "0000-00-00"


            body_str = ""
            for p in body:
                if not body_str:
                    body_str += p
                else:
                    body_str = body_str + " " + p
            for l in linkedwords:
                if not body_str:
                    body_str += l
                else:
                    body_str = body_str + " " + l



            item = {}
            item["title"] = title
            item["author"] = "no_author"
            item["date_published"] = date_published
            item["url"] = response.url
            item["article_text"] = body_str
            item["source"] = "sueddeutsche, DPA"

            yield item


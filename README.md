# NewsWebcrawler

Ein Webcrawler, welcher kostenfreie Nachrichtenartikel über China von drei deutschen Zeitungen sammelt (im Zeitraum Jan. 2020 - Dez. 2021).

Ausführen der Dateien im Terminal: scrapy runspider tagesspiegelspider.py -o result.csv (analog für alle Spider)
Die Pfadangaben müssen modifiziert werden.
Vor dem Ausführen muss im jeweiligen Programm die gewünschte Kategorie gewählt werden.

Die Datei all_articles.csv bildet die Grundlage für eine Nachrichtenanalyse mittels Latent Dirichlet Allocation (siehe  https://github.com/juliakarst/NewsLDA.).

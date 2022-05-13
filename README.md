# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa opini|Selektor|Nazwa zmiennej|Typ danych|
|--------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion||                                
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id||
|autor opinii|span.user-post__author-name|author||
|rekomendacja autora|span.user-post__author-recomendation > em|recommendation||
|liczba gwiazdek|span.user-post__score-count|stars||
|treść opinii|div.user-post__text|content||
|lista zalet|div[class$=positives] ~ div.review-feature__item|pros||
|lista wad|div[class$=negatives] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|span.user_post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|span.user_post__published > time:nth-child(2)\["datetime"\]|purchased||

## Etapy pracy nad projektem strukturalnym
1. Pobranie elementów pojedyńczej opinii do niezależnych zmiennych
2. Zapisanie wszystkich elementów pojedyńczej opinii do jednej zmiennej \(słownik\)
3. Pobranie wszystkich opinii z pojedyńczej strony do słowników i dodanie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku
5. Dodanie możliwości podania id produktu przez użytkownika za pomocą klawiatury
6. Refaktoryzacja \(optymalizacja\) kodu:
    1. Utworzenie funkcji do pobierania składowych strony HTML
    2. utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    3. zamiana instrukcji pobierających składowe opinii do pojedyńczych zmiennych i tworzących z nich składnik na wyrażenie słownikowe \(dictionary comprehension\) tworzące słownik reprezentujący pojedyńczą 
7. Analiza opinii o wybranym produkcie
    1. Wczytanie opinii o wskazanym produkcie do obiektu DataFrame
    2. Wyliczenie podstawowych statystyk na podstawie opinii
        1. Liczba wszystkich opinii o produkcie
        2. Liczba opinii, w których autor podał list zalet produktu
        3. Liczba opinii, w których autor podał listę wad produktu
        4. Średnia ocen produktu
    3. Przygotowanie wykresów na podstawie zawartości opinii
        1. Udział poszczególnych rekomendacji w ogólnej liczbie opinii
        2. Histogram częstości występowania poszczególnich ocen (liczby gwiazdek)
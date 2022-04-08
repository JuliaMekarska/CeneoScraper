# CeneoScraper

##Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

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

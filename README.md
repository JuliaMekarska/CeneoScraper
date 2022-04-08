# CeneoScraper

##Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa opini|Selektor|Nazwa zmiennej|Typ danych|
|--------------|--------|--------------|----------|
|opinia|div.js_product-review|||                                
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|||
|autor opinii|span.user-post\_\_author-name|||
|rekomendacja autora|span.user-post\_\_author-recomendation > em|||
|liczba gwiazdek|span.user-post\_\_score-count|||
|treść opinii|div.user-post\_\_text|||
|lista zalet| review-feature\_\_col|||
|lista wad| review-feature\_\_col|||
|dla ilu osób przydatna|button.vote-yes > span|||
|dla ilu osób nieprzydatna| button.vote-no > span|||
|data wystawienia opinii|span.user_post\_\_published > time:nth-child(1)\["datetime"\]|||
|data zakupu produktu|span.user_post\_\_published > time:nth-child(2)\["datetime"\]|||

# CeneoScraper

##Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|--------------|--------|--------------|----------|
|opinia|div.js_product-review|||
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|||
|autor opinii|span.user-post__author-name|||
|rekomendacja autora|span.user-post__author-recomendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet|review-feature__col||||
|lista wad|review-feature__col||||
|dla ilu osób przydatna|button.vote-yes > span|||
|dla ilu osób nieprzydatna|button.vote-no > span|||
|data wystawienia opinii|span.user_post__published > time:nth-child(1)\["datetime"\]|||
|data zakupu produktu|span.user_post__published > time:nth-child(2)\["datetime"\]|||

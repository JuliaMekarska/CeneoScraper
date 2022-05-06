from urllib import response
import requests
import json
from bs4 import BeautifulSoup

def get_item(ancestor, selector, attribute = None, return_list = False):
    try:
        if return_list:
            return [item.get_text().strip() for item in ancestor.select(selector)]
        if attribute:
            return ancestor.select_one(selector)[attribute]
        return ancestor.select_one(selector).get_text().strip()
    except (AttributeError, TypeError):
        return None

selectors = {
    "author": ["span.user-post__author-name"],
    "recommendation":["span.user-post__author-recomendation > em"],
    "stars":["span.user-post__score-count"],
    "content":["div.user-post__text"],
    "useful":["button.vote-yes > span"],
    "useless":["button.vote-no > span"],
    "published":["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchased":["span.user-post__published > time:nth-child(2)", "datetime"],
    "pros":["div[class$=positives] ~ div.review-feature__item", None, True],
    "cons":["div[class$=negatives] ~ div.review-feature__item", None, True]
}


id_url = str(input("Enter an id from ceneo: "))
url = f"https://www.ceneo.pl/{id_url}#tab=reviews"
all_opinions = []
while(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')

    opinions = page.select("div.js_product-review")
    for opinion in opinions:        
        single_opinion = {
            key:get_item(opinion, *value)
                for key, value in selectors.items()
        }
        single_opinion["opinion_id"] = opinion["data-entry-id"]
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None

with open(f"opinions/{id_url}.json", "w", encoding ="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)

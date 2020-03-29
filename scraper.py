from bs4 import BeautifulSoup
from multiprocessing import Pool
import json
import time
import requests
import dateformatter

PRODUCT_DATE_CLASS = "imVyfb"
SHOPPING_EXPAND_CLASS = "VZTCjd REX1ub translate-content"
ITEM_STORENAME_CLASS = "sh-osd__seller-link"
ITEM_INITIAL_PRICE_CLASS = "QXiyfd"
ITEM_TOTAL_PRICE_CLASS = "sh-osd__total-price"
ITEM_NAME_CLASS = "BvQan"
ITEM_IMAGE_CLASS = "sh-div__image sh-div__current"

headers = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

def get_items(item, days):
    link = "https://www.google.com/search?tbm=shop&tbs=buy:g,vw:l&q=" + str(item)
    items = scrape_item_links(link, int(days))
    return items

def scrape_item_links(link, max_days_from_now):
    start = time.time()
    
    source = requests.get(link, headers=headers)
    soup = BeautifulSoup(source.content, "html.parser")
    content = soup.find_all(class_=SHOPPING_EXPAND_CLASS)
    urls = [("https://www.google.com" + url.get("href")) for url in content]    
    
    # concurrent scraping
    p = Pool(10)
    items = p.map(scrape_date_links, urls)
    p.terminate()
    p.join()

    items = sorted(items, key = lambda k: k["total_price"])
    items = [item for item in items if item["shipping_days"] <= max_days_from_now]
    
    end = time.time()

    print("Time elapsed: " + str(end - start))
    return items

def scrape_date_links(link):
    source = requests.get(link, headers=headers)
    soup = BeautifulSoup(source.content, "html.parser")
    
    content_dates = soup.find(class_=PRODUCT_DATE_CLASS)
    content_store_name = soup.find(class_=ITEM_STORENAME_CLASS)
    content_item_name = soup.find(class_=ITEM_NAME_CLASS)
    content_initial_price = soup.find(class_=ITEM_INITIAL_PRICE_CLASS)
    content_total_price = soup.find("div", class_=ITEM_TOTAL_PRICE_CLASS)
    content_image = soup.find("img", class_=ITEM_IMAGE_CLASS)

    date = content_dates.text
    shipping_days = dateformatter.get_days_from_now(date) 
    store_name = content_store_name.find("span").text
    item_name = content_item_name.text
    initial_price = content_initial_price.find("div").text
    total_price = content_total_price.text
    image = content_image["src"]

    item_info = {
        "shipping_days": shipping_days,
        "store_name": store_name,
        "item_name": item_name,
        "initial_price": float(initial_price[1:].replace(",", "")),
        "total_price": float(total_price[1:].replace(",", "")),
        "image": image
    }

    return item_info





import pandas as pd
from bs4 import BeautifulSoup as bs 
from  urllib.request import urlopen
import logging
import requests

def get_big_box(flipcart_url):
    try:
        url_client = urlopen(flipcart_url)
        flipcart_page = url_client.read()
        flipcart_html = bs(flipcart_page, 'html.parser')
        big_box = flipcart_html.find_all("div", {"class":"_1AtVbE col-12-12"})
        del big_box[0:2]
        return big_box
    except:
        pass

def get_product_url(product_list):
    url_list = []
    for product in product_list:
        try:
            url_list.append("https://www.flipkart.com" + product.div.div.div.a['href'])
        except:
            pass
    return url_list

def get_detail(product_html):
    detail = {}
    try:
        product_rating = product_html.find_all("div", {"class":"_2d4LTz"})
        product_name = product_html.find_all("span", {"class":"B_NuCI"})
        product_image = product_html.find_all("img", {"class":"_396cs4 _2amPTt _3qGmMb"})
        detail = {"name": product_name[0].text, "image": product_image[0]['src'], "rating": product_rating[0].text}  
    except:
        pass
    return detail
def get_product_info(product_url):
    info = []
    try:
        for url in product_url:
            product_client = urlopen(url)
            product_page = product_client.read()
            product_html = bs(product_page, 'html.parser')
            detail = get_detail(product_html)
            info.append(detail)
    except:
        pass
    return info

def f_main(flipcart_url):
    product_list = get_big_box(flipcart_url)
    url_list = get_product_url(product_list)
    product_detail = get_product_info(url_list)
    return product_detail

'''if __name__ == "__main__":
    flipcart = "https://www.flipkart.com/search?q="+ "iphone11"
    print(main(flipcart))'''

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import json
import requests
import json
import csv
import re
import os
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback
import random
from utils import headers_list
from kafka_producer import produce

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def retryRequest(url):

    headers = random.choice(headers_list)
    # print(user_agent)
    session = requests.Session()
    retry = Retry(connect=4, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # proxies = get_proxies()
    # proxy_pool = cycle(proxies)
    # for i in range(1,11):
    #     #Get a proxy from the pool
    #     proxy = next(proxy_pool)
    #     try:
    #         response = session.get(url, headers=headers,proxies={"http": proxy, "https": proxy})
    #     except:
    #         #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
    #         #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
    #         response = "" 
    #         print("Skipping. Connnection error")
    #     if response != "":
    #         break
    response = session.get(url, headers=headers)

    return response

def crawl_product_id(url,cateid):
    product_list = []
    products = []
    i = 1
    flag = True
    try:
        os.makedirs(f"./data/raw_product/{cateid}")
    except:
        print("Folder exists")
    while (flag):
        print("Crawl page: ", i)
        print(url.format(cateid = cateid,page = i))
        try:
            response = retryRequest(url.format(cateid = cateid,page = i))
        except Exception as e:
            print(e)
            break
        print(response.status_code)
        if (response.status_code != 200):
            break

        products = json.loads(response.text)["data"]
        last_page = json.loads(response.text)["paging"]["last_page"]
        if (i >= last_page):
            flag = False
        with open(f"./data/raw_product/{cateid}/{cateid}-{i}.json","w+") as f:
            json.dump(products,f,indent = 4,ensure_ascii = False)
        if len(products) == 0:
            break
        i += 1
        try:
            for product in products:
                # print(product)
                produce("sample",product)
        except Exception as e:
            print(e)

    return product_list,products, i

def crawl_single_product(url,product_id):

    product_detail = " "
    url = url.format(product_id)
    response = retryRequest(url)
    if (response.status_code == 200):
        # product_detail_list.append(response.text)
        product_detail = response.text
        print("Crawl product: ", product_id, ": ", response.status_code)

    return product_detail

def crawl_product(url,product_list=[]):
    product_detail_list = []
    for product_id in product_list:
        product_detail = crawl_single_product(url,product_id)
        product_detail_list.append(product_detail)
    return product_detail_list

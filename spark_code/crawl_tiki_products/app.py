from utils import *
import logging
import os
# from time import time
import time
from queue import Queue
from threading import Thread
from crawler_product import *
from kafka_producer import produce
import pandas as pd 

all_cat = []
df = pd.read_csv("tiki_cat_new.csv")
for cat in df["cate_id"]:
    all_cat.append(cat)
parentCategory = ["1789","4221","1815","1846","1801","4384","2549","1520","1975","8594","8322"]

# parentCategory = ["1815","1801"]
cate_url = "https://tiki.vn/api/v2/products?limit=48&include=advertisement&aggregations=1&category={cateid}&page={page}"
product_url = "https://tiki.vn/api/v2/products/{}"
flatten_field = [ "badges", "inventory", "categories", "rating_summary", 
                      "brand", "seller_specifications", "current_seller", "other_sellers", 
                      "configurable_options",  "configurable_products", "specifications", "product_links",
                      "services_and_promotions", "promotions", "stock_item", "installment_info" ]

# class DownloadWorker(Thread):
    
#     def __init__(self, queue):
#         Thread.__init__(self)
#         self.queue = queue

#     def run(self):
#         while True:
#             # Get the work from the queue and expand the tuple
#             product_id = self.queue.get()
#             try:
#                 crawl_single_product(product_url,product_id)
#             finally:
#                 self.queue.task_done()

class ProductWorker(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            cate_id = self.queue.get()
            try:
                crawl_product_id(cate_url,cate_id)
            finally:
                self.queue.task_done()

def multiThreadScraper(ThreadObject,argList):
    # product_list = load_raw_product("./data/product_id/{}.txt".format("1789"))
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 4 worker threads
    for x in range(4):
        worker = ThreadObject(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    for id in argList:
        # logger.info('Queueing {}'.format(id))
        queue.put((id))
        # product_detail_list.append(product)
    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()

    # logging.info('Took %s seconds', time() - ts)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    multiThreadScraper(ProductWorker,all_cat[370::])
    # print(all_cat)







    


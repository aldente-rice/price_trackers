import pandas as pd
import matplotlib
import csv
from store_tracker import track_bestbuy, track_amazon, bestbuy_to_amazon, amazon_to_bestbuy
from datetime import datetime


# pd.set_option('display.max_columns', None) # displays all columns
# pd.set_option('display.width', 150) # max number of chars displayed in a line (for .head())
# df = pd.read_csv('price_data.csv')
# print(df.head())

# Gets the current date and time 'MM/DD/YYYY HH:MM'
now = datetime.now().strftime("%m/%d/%Y %H:%M")
# x = now.strftime("%m/%d/%Y %H:%M")
# x.split()
# date = x.split()[0]
# time = x.split()[1]
# print(x.split())

data = []

# [model_num, model_sku, price, item_title]
description = track_bestbuy("https://www.bestbuy.com/site/apple-airpods-4-white/6447384.p?skuId=6447384")
data.append({"time":now, "model_num":description[0], "model_sku":description[1],
             "price":description[2], "item_title":description[3]})

df = pd.DataFrame(data)
print(df.head())


# Gathers information (price, URLs, date modified)
# temp_link_bb:str = 'https://www.bestbuy.com/site/apple-airpods-4-white/6447384.p?skuId=6447384'
# price_1:float = track_bestbuy(temp_link_bb)
# temp_link_am:str = bestbuy_to_amazon(temp_link_bb)
# # print(temp_link_am)
# price_2:float = track_amazon(temp_link_am)

# print(price_1)
# print(price_2)

# data = {
#     'item_name':price_1[1],
#     'bestbuy_url':temp_link_bb,
#     'bestbuy_price':price_1[0],
#     'amazon_url':temp_link_am,
#     'amazon_price':price_2[0],
#     'price_diff':abs(price_1[0] - price_2[0]),
#     'time_updated': '2/25/2025',
#     'date_updated': '15:48'
# }

# with open('price_data.csv', 'a') as f:
#     f.write(data)

# columns: item_name, bestbuy_url, bestbuy_price, amazon_url, amazon_price, price_diff, time_updated, date_updated
# fields=[price_1[1], temp_link_bb, price_1[0], temp_link_am, price_2[0],
#         abs(price_1[0] - price_2[0]), time, date]

# the r before file name is to avoid escape characters
# with open(r'price_data.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(fields)
#
# df = pd.read_csv('price_data.csv')
# print(df.head())


# @parameters
# item_url: the item url of where the users retrieved the item
# store: the website the user retrieved the item from (Amazon or Bestbuy)
#
# price track interval: 1 hour (for now, every 2 minutes to get data)
#
# keeps track of an item from either Amazon or Bestbuy
# stores the data to then visualize data
def track_price(item_url, store):
    return None


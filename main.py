import pandas as pd
import matplotlib
from store_tracker import track_bestbuy, track_amazon, bestbuy_to_amazon, amazon_to_bestbuy


pd.set_option('display.max_columns', None) # displays all columns
pd.set_option('display.width', 100) # max number of chars displayed in a line (for .head())
df = pd.read_csv('price_data.csv')
print(df.head())

# gathers information (price, URLs, date modified)
temp_link_bb = 'https://www.bestbuy.com/site/apple-airpods-4-white/6447384.p?skuId=6447384'
price_1 = track_bestbuy(temp_link_bb)
temp_link_am = bestbuy_to_amazon(temp_link_bb)
# print(temp_link_am)
price_2 = track_amazon(temp_link_am)

print(price_1)
print(price_2)

# print(df.head())


# @parameters
# item_url: the item url of where the users retrieved the item
# store: the website the user retrieved the item from (Amazon or Bestbuy)
#
# price track interval: 1 hour
#
# keeps track of an item from either Amazon or Bestbuy
# stores the data to then visualize data
def track_price(item_url, store):
    return None



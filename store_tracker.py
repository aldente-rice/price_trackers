import selenium
import time
import selenium.webdriver.firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


def track_best_buy(item_url) -> float:
    driver = webdriver.Firefox()
    driver.get(item_url)
    time.sleep(0.5)

    price_element = driver.find_element(By.CLASS_NAME, 'priceView-hero-price')
    price = price_element.find_element(By.TAG_NAME, 'span').text
    price = price.replace(',', '')
    price = price.replace('$', '')
    price = float(price)
    driver.quit()

    return price

# x = track_best_buy('https://www.bestbuy.com/site/razer-blade-16-16-gaming-laptop-dual-mini-led-4k-uhd-fhd-intel-i9-hx-nvidia-geforce-rtx-4080-32gb-ram-2tb-ssd-mercury/6570244.p?skuId=6570244')
# print(x)


def track_amazon(item_url) -> float:

    price = 0

    return price


# not all products are available on one or both websites
# likely discontinued or something
def bestbuy_to_amazon(item_url) -> str:
    return ""


def amazon_to_bestbuy(item_url) -> str:
    return ""




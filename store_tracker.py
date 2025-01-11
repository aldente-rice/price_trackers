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


# x = track_best_buy('https://www.bestbuy.com/site/razer-blade-16-16-gaming-laptop-dual-mini-led-4k-uhd-fhd-intel-i9'
#                    '-hx-nvidia-geforce-rtx-4080-32gb-ram-2tb-ssd-mercury/6570244.p?skuId=6570244')
# print(x)


def track_amazon(item_url) -> float:
    driver = webdriver.Firefox()
    driver.get(item_url)
    time.sleep(0.5)

    price_element = driver.find_element(By.CLASS_NAME, 'a-price-whole')
    price = float(price_element.text)
    price_cent_element = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
    price += float(price_cent_element.text) * 0.01
    driver.quit()

    return price


# y = track_amazon('https://www.amazon.com/Racing-Gaming-Simulator-Bundle-Steering-PC/dp/B07DW25P3R/ref=pd_ci'
#                  '_mcx_mh_mcx_views_0_image?pd_rd_w=xWTd6&content-id=amzn1.sym.bb21fc54-1dd8-448e-92bb-2ddce18'
#                  '7f4ac%3Aamzn1.symc.40e6a10e-cbc4-4fa5-81e3-4435ff64d03b&pf_rd_p=bb21fc54-1dd8-448e-92bb-2ddce'
#                  '187f4ac&pf_rd_r=4NRGP0335XRVF31DS8ZQ&pd_rd_wg=Pambw&pd_rd_r=e2331406-455b-4c44-9472-b10c8e1'
#                  'bab54&pd_rd_i=B07DW25P3R&th=1')
# print(y)


# not all products are available on one or both websites
# likely discontinued or something
def bestbuy_to_amazon(item_url) -> str:
    return ""


def amazon_to_bestbuy(item_url) -> str:
    return ""




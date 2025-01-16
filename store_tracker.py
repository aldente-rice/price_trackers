import selenium
import time
import selenium.webdriver.firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
    price += float(price_cent_element.text) * 0.01  # convert to cents
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
# takes in a link from bestbuy.com and outputs a string to amazon.com
# finds the best match based on the product item
# looks at the first three results to find the closest match to the item title from BestBuy
def bestbuy_to_amazon(item_url) -> str:
    driver = webdriver.Firefox()
    driver.get(item_url)
    time.sleep(0.5)

    item_title = driver.find_element(By.CLASS_NAME, 'heading-4').text
    # driver.quit()

    # searches for the item's title that was retrieved on the searchbar
    driver.get('https://www.amazon.com/')
    time.sleep(2)
    driver.implicitly_wait(1)

    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    # )

    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').click()
    # search_bar.find_element(By.ID, 'twotabsearchtextbox').click()
    # driver.find_element(By.ID, 'twotabsearchtextbox')
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(item_title, Keys.ENTER)
    time.sleep(2)

    # finds the best match of the first three results
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span'))
    )
    # print(type(item))

    a = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[5]/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span')
    print(a.text)
    # print(type(a))

    # retrieves the current url from amazon.com of the matching product
    item_to_amazon = driver.current_url

    driver.quit()

    return item_to_amazon


x = bestbuy_to_amazon('https://www.bestbuy.com/site/apple-10-9-inch-ipad-latest-model-10th-generation-with-wi-fi-64gb-pink/5201002.p?skuId=5201002')
print(x)


# takes in a link from amazon.comb and outputs a string to bestbuy.com
# finds the best match based on the product item
def amazon_to_bestbuy(item_url) -> str:
    return ""

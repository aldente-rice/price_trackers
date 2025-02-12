import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from amazoncaptcha import AmazonCaptcha


# takes in a user-input url
# scrapes Best Buy for the price and the item name
#
# @returns
# price: the price (float)
# item_title: the product listing name (str)
def track_best_buy(item_url) -> [float, str]:
    driver = webdriver.Firefox()
    driver.get(item_url)
    time.sleep(0.5)

    item_title = driver.find_element(By.CLASS_NAME, 'heading-4').text

    price_element = driver.find_element(By.CLASS_NAME, 'priceView-hero-price')
    price = price_element.find_element(By.TAG_NAME, 'span').text
    price = price.replace(',', '')
    price = price.replace('$', '')
    price = float(price)
    driver.quit()

    return [price, item_title]


# x = track_best_buy('https://www.bestbuy.com/site/razer-blade-16-16-gaming-laptop-dual-mini-led-4k-uhd-fhd-intel-i9'
#                    '-hx-nvidia-geforce-rtx-4080-32gb-ram-2tb-ssd-mercury/6570244.p?skuId=6570244')
# print(x)


# takes in a user-input url
# scrapes Amazon for the price and the item name
#
# @returns
# price: the price (float)
# item_title: the product listing name (str)
def track_amazon(item_url) -> [float, str]:
    driver = webdriver.Firefox()
    driver.get(item_url)
    time.sleep(0.5)

    item_title = driver.find_element(By.ID, 'productTitle').text

    price_element = driver.find_element(By.CLASS_NAME, 'a-price-whole')
    price = float(price_element.text)
    price_cent_element = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
    price += float(price_cent_element.text) * 0.01  # convert to cents
    driver.quit()

    return [price, item_title]


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
# looks at the first few results to find the closest match to the item title from BestBuy (that aren't sponsored)
def bestbuy_to_amazon(item_url) -> str:
    driver = webdriver.Firefox()
    driver.get(item_url)
    time.sleep(0.5)

    item_title = driver.find_element(By.CLASS_NAME, 'heading-4').text
    # driver.quit()

    # searches for the item's title that was retrieved on the searchbar
    driver.get('https://www.amazon.com/')
    driver.implicitly_wait(1)
    # remove captcha, test to see if captcha exists first
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.a-row:nth-child(2) > img:nth-child(1)'))
    )

    try:
        captcha_img = driver.find_element(By.XPATH,
                                          '/html/body/div/div[1]/div[3]/div/div/form/div[1]'
                                        '/div/div/div[1]/img').get_attribute('src')
        captcha = AmazonCaptcha.fromlink(captcha_img)
        solution = captcha.solve()

        driver.find_element(By.ID, 'captchacharacters').click()
        driver.find_element(By.ID, 'captchacharacters').send_keys(solution, Keys.ENTER)
        driver.implicitly_wait(1)
    except NoSuchElementException:
        print('No Captcha Found (Amazon)\n')

    # find and click on Amazon's search bar
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').click()

    # search_bar.find_element(By.ID, 'twotabsearchtextbox').click()
    # driver.find_element(By.ID, 'twotabsearchtextbox')
    driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]').send_keys(item_title, Keys.ENTER)
    time.sleep(2)

    # finds the best match of the first three results
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/
    #                                               div[2]/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span'))
    # )
    # print(type(item))

    # gets the first few results title from Amazon (not sponsored listings)
    # can be used to find best result, but for now, we are only using the first result
    results = {}
    for i in range(2, 6):
        try:
            # find the listing's title
            result_title = driver.find_element(By.XPATH,f'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/'
                                                        f'div[1]/div[{i}]/div/div/span/div/div/div/div[2]/div/div/'
                                                        f'div[1]/a/h2/span')
            # if element is 'sponsored', skip over it
        except NoSuchElementException:
            continue
        # add title (key) to results with the index that it was founded (value)
        results[result_title] = i

    # prints the results title of the listings
    # for item in results:
    #     print(item.text)

    # retrieves the current url from amazon.com of the matching product
    click_index = list(results.values())[0]
    driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/'
                                        f'div[1]/div[{click_index}]/div/div/span/div/div/div/div[2]/div/div/'
                                        f'div[1]/a/h2/span').click()
    driver.implicitly_wait(1)
    item_to_amazon = driver.current_url
    driver.quit()

    return item_to_amazon

# testing getting amazon link
# x = bestbuy_to_amazon('https://www.bestbuy.com/site/apple-airpods-4-white/6447384.p?skuId=6447384')
# print(x)


# takes in a link from amazon.comb and outputs a string to bestbuy.com
# finds the best match based on the product item
#
def amazon_to_bestbuy(item_url) -> str:
    driver = webdriver.Firefox()
    driver.get(item_url)
    time.sleep(0.5)

    # remove captcha, test to see if captcha exists first
    try:
        captcha_img = driver.find_element(By.XPATH, '//*[@div="a-row a-text-center"]//img').get_attribute('src')
        captcha = AmazonCaptcha.fromlink(captcha_img)
        solution = captcha.solve()

        driver.find_element(By.ID, 'captchacharacters').click()
        driver.find_element(By.ID, 'captchacharacters').send_keys(solution, Keys.ENTER)
        driver.implicitly_wait(1)
    except NoSuchElementException:
        print('No Captcha Found (Amazon)\n')

    item_title = driver.find_element(By.ID, 'productTitle').text
    # print(item_title)
    driver.get('https://www.bestbuy.com/')
    driver.implicitly_wait(1)

    driver.find_element(By.ID, 'gh-search-input').click()
    driver.find_element(By.ID, 'gh-search-input').send_keys(item_title)
    driver.find_element(By.CLASS_NAME, 'header-search-button').click()
    driver.implicitly_wait(1)
    driver.find_element(By.CLASS_NAME, 'product-image ').click()

    # find_price = driver.find_element(By.CLASS_NAME, 'priceView-hero-price').text.split()
    # price = float(find_price[0][1:])
    # print(price, ' | type is: ', type(price))

    item_to_bestbuy = driver.current_url
    driver.quit()

    return item_to_bestbuy

# print(amazon_to_bestbuy('https://www.amazon.com/Apple-Headphones-Cancellation-Transparency-Personalized/dp/B0DGJ7HYG1/ref=sr_1_1?crid=227UOL5IM75V4&dib=eyJ2IjoiMSJ9.ilo9fkrYdOqmSNlTL9iUbgoVlb9Bg0ObgIWOyfyuZDXu3z5czi-xnqWEtM3kqxwP89dgikoLr7TM-ND4m0YwqM2ncKOcPpyOA0zm7U5wn3sBFsaWM7iP6q0Q_RxYsiDno1nDX8Tl4fnmBb8xUeBhl62spKRgtAWvQkYAf8Xippt23yIZIb5-MzFuSA_Dkm1ThK2-w_44IknZqCbwSJznWGv1Bv9-wdTUmNAmc39C2Y8.DaeCRXojLw6fxGnM-600uWls9_taH3tNfHmoucIBYW8&dib_tag=se&keywords=air%2Bpods%2B4&qid=1739046304&sprefix=air%2Bpods%2B4%2Caps%2C82&sr=8-1&th=1'))
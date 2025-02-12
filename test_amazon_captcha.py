import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from amazoncaptcha import AmazonCaptcha


driver = webdriver.Firefox()
driver.get('https://www.amazon.com/errors/validateCaptcha')


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div.a-row:nth-child(2) > img:nth-child(1)'))
)

try:
    captcha_img = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img').get_attribute('src')
    captcha = AmazonCaptcha.fromlink(captcha_img)
    solution = captcha.solve()

    driver.find_element(By.ID, 'captchacharacters').click()
    driver.find_element(By.ID, 'captchacharacters').send_keys(solution, Keys.ENTER)
    driver.implicitly_wait(1)
except NoSuchElementException:
    print('No Captcha Found (Amazon)\n')
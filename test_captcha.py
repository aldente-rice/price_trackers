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
    EC.presence_of_element_located((By.CLASS_NAME, 'a-row a-text-center'))
)
try:
    captcha_img = driver.find_element(By.XPATH, '//*[@div="a-row a-text-center"]//img').get_attribute('src')
    captcha = AmazonCaptcha.fromlink(captcha_img)
    solution = captcha.solve()

    driver.find_element(By.ID, 'captchacharacters').click()
    driver.find_element(By.ID, 'captchacharacters').send_keys(solution, Keys.ENTER)
    driver.implicitly_wait(1)
except NoSuchElementException:
    print('No Captcha Found (Amazon)\n')
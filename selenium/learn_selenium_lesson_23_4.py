import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    # click on button
    browser.find_element(By.TAG_NAME, 'button').click()

    # accept confirm
    browser.switch_to.alert.accept()

    input_number = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(input_number))
    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(10)






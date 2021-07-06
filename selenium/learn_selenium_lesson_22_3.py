import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return x + y


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/selects2.html')

    x = int(browser.find_element_by_id('num1').text)
    y = int(browser.find_element_by_id('num2').text)
    answer = calc(x, y)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(answer))

    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(7)






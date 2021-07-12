import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_css_selector('button.trollface').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_css_selector('button.btn').click()

    time.sleep(7)






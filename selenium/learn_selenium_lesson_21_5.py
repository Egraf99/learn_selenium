import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/math.html')
    input_number = browser.find_element_by_css_selector('div.form-group span#input_value').text
    browser.find_element_by_css_selector('input#answer').send_keys(calc(input_number))
    browser.find_element_by_css_selector('input[type="checkbox"]').click()
    browser.find_element_by_css_selector('input#robotsRule[type="radio"]').click()
    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(10)
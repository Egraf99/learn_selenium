import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    button = browser.find_element_by_css_selector('button.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x = browser.find_element_by_id('input_value').text
    answer = calc(x)
    browser.find_element_by_id('answer').send_keys(answer)

    browser.execute_script('window.scrollBy(0, 250);')
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    button.click()

    time.sleep(7)






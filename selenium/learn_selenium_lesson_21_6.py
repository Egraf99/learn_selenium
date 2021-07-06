import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/math.html')
    people_radio = browser.find_element_by_id('peopleRule')
    people_checked = people_radio.get_attribute('checked')
    print('value of people radio: ', people_checked)

    robot_checked = browser.find_element_by_id('robotsRule').get_attribute('checked')
    print('value of robot radio: ', robot_checked)

    submit_checked = browser.find_element_by_css_selector('button.btn').get_attribute('disabled')
    print('value of submit button: ', submit_checked)

    time.sleep(11)

    submit_checked = browser.find_element_by_css_selector('button.btn').get_attribute('disabled')
    print('value of submit button: ', submit_checked)

from selenium import webdriver
import time

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for el in elements:
        el.send_keys("Бе")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(30)

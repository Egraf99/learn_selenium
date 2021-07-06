import math
import time
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element_by_xpath("//div[@class='form-group']/input[@name='firstname' and @required]").\
        send_keys('FirstName')
    browser.find_element_by_xpath("//div[@class='form-group']/input[@name='lastname' and @required]").\
        send_keys('LastName')
    browser.find_element_by_xpath("//div[@class='form-group']/input[@name='email' and @required]").\
        send_keys('Email')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_css_selector('input[type="file"]').send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn-primary')
    button.click()

    time.sleep(7)






import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return x + y


with webdriver.Chrome() as browser:
    browser.execute_script('''document.title="Script executing";
                              alert("Robots as work");''')

    time.sleep(7)






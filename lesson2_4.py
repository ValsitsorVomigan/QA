﻿from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    var = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    button = browser.find_element_by_css_selector('#book')

    button.click()

    x__ = browser.find_element_by_css_selector('#input_value')
    x_ = x__.text
    x = calc(x_)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(x)

    button1 = browser.find_element_by_css_selector('#solve')
    button1.click()
finally:
    time.sleep(10)
    browser.quit()

    




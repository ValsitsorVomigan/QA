from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value__ = browser.find_element_by_css_selector('#input_value')
    value_ = value__.text
    value = calc(value_)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(value)

    button = browser.find_element_by_css_selector("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    time.sleep(1)

    radio = browser.find_element_by_css_selector("#robotsrule")
    radio.click()

    time.sleep(1)

    
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()

    




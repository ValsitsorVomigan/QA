from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)
    
    time.sleep(1)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    time.sleep(1)

    radio = browser.find_element_by_css_selector("#robotsrule")
    radio.click()

    time.sleep(1)

    button = browser.find_element_by_css_selector("button")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()




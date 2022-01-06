from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()
    
    x__ = browser.find_element_by_css_selector("#input_value")
    x_ = x__.text
    x = calc(x_)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(x)

    time.sleep(1)

    button = browser.find_element_by_css_selector("button")
    button.click()
        
finally:
    time.sleep(10)
    browser.quit()

    




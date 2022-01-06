from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_e = browser.find_element_by_css_selector('#num1')
    y_e = browser.find_element_by_css_selector('#num2')
    x = x_e.text
    y = y_e.text
    sum = str(int(x) + int(y))
    
    time.sleep(1)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum) 
    
    button = browser.find_element_by_css_selector("button")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()




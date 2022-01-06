import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num_list = ['first', 'second', 'third']
    for num in num_list:
        element = browser.find_element_by_css_selector(".first_block .form-control.{}".format(num))
        element.send_keys("ASS")
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()


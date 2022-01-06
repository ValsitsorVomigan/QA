from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("mail@mail.ru")

    time.sleep(1)

    fileform = browser.find_element_by_css_selector('[name="file"]')
    fileform.send_keys('C:/Users/Rostislav/file.txt')

    button = browser.find_element_by_css_selector("button")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()

    




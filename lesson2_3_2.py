from selenium import webdriver
import time


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("button")
   
     
finally:
    time.sleep(10)
    browser.quit()

    




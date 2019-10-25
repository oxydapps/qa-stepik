from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try: 
    
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector("input[name='firstname']")
    element1.send_keys("Test")
    element2 = browser.find_element_by_css_selector("input[name='lastname']")
    element2.send_keys("Secondtest")
    element3 = browser.find_element_by_css_selector("input[name='email']")
    element3.send_keys("test@gmail.com")

    element4 = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()


finally:
    time.sleep(5)
    browser.quit()

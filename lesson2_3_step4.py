from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
try: 
    
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    element1 = browser.find_element_by_id("input_value")
    x = element1.text
    y = calc(x)

    element_input = browser.find_element_by_id("answer")
    element_input.send_keys(y)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()



finally:
    time.sleep(5)
    browser.quit()
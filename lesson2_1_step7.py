from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_id("treasure")
    x = element1.get_attribute("valuex")
    y = calc(x)

    element_input = browser.find_element_by_id("answer")
    element_input.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()



    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()



finally:
    time.sleep(5)
    browser.quit()

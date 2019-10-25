from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try: 

    browser = webdriver.Chrome()
    browser.get(link)

    find_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element_by_id("book")
    button1.click()

    element1 = browser.find_element_by_id("input_value")
    x = element1.text
    y = calc(x)

    element_input = browser.find_element_by_id("answer")
    element_input.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
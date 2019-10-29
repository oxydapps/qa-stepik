from selenium import webdriver
import time

def run_browser(link):
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector(".first_block .first")
    element1.send_keys("Test")
    element2 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    element2.send_keys("Secondtest")
    element3 = browser.find_element_by_class_name("third")
    element3.send_keys("test@gmail.com")
    element4 = browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control first']")
    element4.send_keys("+123456789109")
    element5 = browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control second']")
    element5.send_keys("Testcity")  

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)


    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    browser.quit()

    return welcome_text


def test_abs1(self):
    message = "Congratulations! You have successfully registered!"
    assert run_browser("http://suninjuly.github.io/registration1.html") == message, "Should be successfull message"

def test_abs2(self):
    message = "Congratulations! You have successfully registered!"
    assert run_browser("http://suninjuly.github.io/registration2.html") ==  message, "Should be successfull message"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
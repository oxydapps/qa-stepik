from selenium import webdriver
import time

try: 
    #old link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration1.html"
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


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

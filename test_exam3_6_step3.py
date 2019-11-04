import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

col_urls = (895, 896, 897, 898, 899, 903, 904, 905)
ans = []

@pytest.mark.parametrize("number", col_urls)
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/236{number}/step/1"
    browser.get(link)
    text_input = browser.find_element_by_css_selector(".textarea.ember-text-area.ember-view")
    answer = math.log(int(time.time()))
    text_input.send_keys(str(answer))
    button_send = browser.find_element_by_class_name("submit-submission")
    button_send.click()
    text_ans = browser.find_element_by_class_name("smart-hints__hint")
    assert text_ans.text == "Correct!"


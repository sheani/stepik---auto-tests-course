import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    time.sleep(6)

    input_answer = browser.find_element_by_xpath('//html/body/div/div[1]/div[2]/main/div/div[2]/div[2]/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[2]/div[2]/div/div/div/textarea')
    answer = math.log(int(time.time()))
    input_answer.send_keys(str(answer))
    
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(3)
    
    str_0 = browser.find_element_by_xpath('//html/body/div/div[1]/div[2]/main/div/div[2]/div[2]/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div/pre')
    assert str_0.text == 'Correct!', f"{str_0.text}"
    time.sleep(1)

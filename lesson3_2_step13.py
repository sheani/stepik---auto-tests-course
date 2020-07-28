from selenium import webdriver
import time
import unittest
class TestAbs(unittest.TestCase):
	def test_abs1(self):

		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		element1 = browser.find_element_by_xpath('//div[@class="first_block"]/div[1]/input')
		element1.send_keys("Alya")
		element2 = browser.find_element_by_xpath('//div[@class="first_block"]/div[2]/input')
		element2.send_keys("Nikiforova")
		element3 = browser.find_element_by_xpath('//div[@class="first_block"]/div[3]/input')
		element3.send_keys("aaa@gmail.com")
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
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test failed!")

		# ожидание чтобы визуально оценить результаты прохождения скрипта
		time.sleep(3)
		# закрываем браузер после всех манипуляций
		browser.quit()

	def test_abs2(self):

		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		element1 = browser.find_element_by_xpath('//div[@class="first_block"]/div[1]/input')
		element1.send_keys("Alya")
		element2 = browser.find_element_by_xpath('//div[@class="first_block"]/div[2]/input')
		element2.send_keys("aaa@gmail.com")
		element3 = browser.find_element_by_xpath('//div[@class="first_block"]/div[3]/input')
		element3.send_keys("aaa@gmail.com")

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
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test failed!")

		# ожидание чтобы визуально оценить результаты прохождения скрипта
		time.sleep(3)
		# закрываем браузер после всех манипуляций
		browser.quit()


if __name__ == "__main__":
	unittest.main()


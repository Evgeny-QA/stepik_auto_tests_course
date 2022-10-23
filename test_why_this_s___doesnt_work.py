import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()


class TestAbs(unittest.TestCase):
    def test_first_reg_link(self):
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
        input3.send_keys("123@email")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"expected 'Congratulations! You have successfully registered!' instead '{welcome_text}'")

    def test_second_reg_link(self):
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
        input3.send_keys("IvaPet@email.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f"expected 'Congratulations! You have successfully registered!' instead '{welcome_text}'")


if __name__ == "__main__":
    unittest.main()
time.sleep(20)
browser.quit()

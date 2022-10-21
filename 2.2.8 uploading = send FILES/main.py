from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("Zhenya")
    browser.find_element(By.NAME, "lastname").send_keys("Evg")
    browser.find_element(By.NAME, "email").send_keys("123@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, 'file.txt')
    #browser.find_element(By.ID, "file").click()  NOT!!!!
    browser.find_element(By.ID, "file").send_keys(file)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(8)
    browser.quit()

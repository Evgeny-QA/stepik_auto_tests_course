from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    answer = str(int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(answer)
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(6)
    browser.quit()

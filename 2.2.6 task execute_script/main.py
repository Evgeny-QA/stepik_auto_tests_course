from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value").text
    x = calc(x)
    browser.execute_script("window.scrollBy(0, 120);")
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(x)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(8)
    browser.quit()

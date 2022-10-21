from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.CSS_SELECTOR, ".nowrap#input_value").text
    x = calc(x)
    browser.find_element(By.ID, "answer").send_keys(x)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(8)
    browser.quit()

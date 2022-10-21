from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    people_radio = browser.find_element(By.ID, "treasure")
    people_checked = people_radio.get_attribute("valuex")
    x = calc(people_checked)
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
    time.sleep(10)
    browser.quit()

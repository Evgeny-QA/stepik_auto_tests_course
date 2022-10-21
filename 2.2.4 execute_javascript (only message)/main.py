from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(6)
    browser.quit()

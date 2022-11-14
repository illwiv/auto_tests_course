from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    field_element = browser.find_element(By.ID, "answer")
    field_element.send_keys(y)
    button_second = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_second.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

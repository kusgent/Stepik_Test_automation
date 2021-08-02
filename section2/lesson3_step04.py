# https://stepik.org/lesson/184253/step/4?unit=158843

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    browser.find_element_by_css_selector(".btn").click()

    browser.switch_to.alert.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
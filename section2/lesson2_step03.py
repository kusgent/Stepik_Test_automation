# https://stepik.org/lesson/228249/step/3?unit=200781

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    # link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1_el = browser.find_element_by_id("num1")
    number1 = int(number1_el.text)

    number2_el = browser.find_element_by_id("num2")
    number2 = int(number2_el.text)

    amount = str(number1 + number2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(amount)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
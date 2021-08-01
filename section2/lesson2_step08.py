# https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ilya")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Kustov")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("test@test.com")

    file_upload = browser.find_element_by_id("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')
    file_upload.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
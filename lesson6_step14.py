from selenium import webdriver

import time

import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

 

link = " http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[name = 'firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name = 'lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[name = 'email']")
    input3.send_keys("info@gmail.com")

    
    

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    
    time.sleep(300)

    browser.quit()
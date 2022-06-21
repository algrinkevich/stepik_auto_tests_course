import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_value = browser.find_element(By.ID,"input_value")
    x = x_value.text
    y = calc(x)
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)
    robot_checkbox = browser.find_element(By.ID,"robotCheckbox")
    robot_checkbox.click()
    robot_radio = browser.find_element(By.ID, "robotsRule")
    robot_radio.click()
    submit_btn = browser.find_element(By.CLASS_NAME, "btn")
    submit_btn.click()
finally:
    # waiting for a few seconds to get an answer from the alert
    time.sleep(5)
    browser.quit()



import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price_label = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_btn = browser.find_element(By.ID, "book")
    book_btn.click()
    x_value = browser.find_element(By.ID, "input_value")
    x = x_value.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    submit_btn = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    submit_btn.click()
finally:
    # waiting for a few seconds to get an answer from the alert
    time.sleep(5)
    browser.quit()

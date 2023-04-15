import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x) 
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    radiobutton = browser.find_element(By.ID, "robotsRule").click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

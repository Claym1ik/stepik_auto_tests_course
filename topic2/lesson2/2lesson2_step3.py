import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    find_number1 = browser.find_element(By.ID, "num1")
    number1 = find_number1.text
    find_number2 = browser.find_element(By.ID, "num2")
    number2 = find_number2.text
    x = str(int(number1)+int(number2))
    

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

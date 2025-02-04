from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver =  webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver/chromedriver-win64/chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Explicit Wait

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.CLASS_NAME, "submit-button btn_action"))
finally:
    driver.quit()


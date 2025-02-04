import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.javatpoint.com/python-tutorial")
print(driver.title)

driver.get("https://www.javatpoint.com/numpy-tutorial")
time.sleep(3)
print(driver.title)

driver.back()           #navigation command
time.sleep(3)
print(driver.title)
driver.forward()        #navigation command
time.sleep(3)
print(driver.title)

driver.close()




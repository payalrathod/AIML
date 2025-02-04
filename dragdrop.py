import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://formy-project.herokuapp.com/dragdrop")

abc1 = driver.find_element_by_id("image")
abc2 = driver.find_element_by_id("box")

action = ActionChains(driver)
action.drag_and_drop(abc1, abc2).perform()

time.sleep(2)
driver.close()




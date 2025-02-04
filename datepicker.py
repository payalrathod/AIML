from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://formy-project.herokuapp.com/datepicker")

abc = driver.find_element_by_id("datepicker")
abc.send_keys("03/03/2021")
abc.send_keys(Keys.RETURN)







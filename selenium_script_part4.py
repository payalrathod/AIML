from datetime import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.browserstack.com/users/sign_in")

abc = driver.find_element_by_name("user[login]")         #the name of element
print(abc.is_displayed())           #returns true or false based on element status
print(abc.is_enabled())             #returns true or false

bcd = driver.find_element_by_name("user[password]")
print(bcd.is_displayed())           #returns true or false based on element status
print(bcd.is_enabled())             #returns true or false

abc.send_keys("payal.rakeshrathod@gmail.com")
bcd.send_keys("Pass@123")

#driver.find_element_by_name("commit").click()
#driver.find_element_by_id("user_submit").click()
#driver.find_element_by_css_selector("").click()

time.sleep(9)
#clicking on the button
# button = driver.find_elements_by_xpath("//*[@id='user_submit']")
# button.click()

driver.find_element_by_id("accept-cookie-notification").click()
driver.find_element_by_id("user_submit").click()

#driver.find_element_by_id().get_attribute()
#driver.switch_to.alert()

driver.maximize_window()    #maximize the window size
# driver.minimize_window()    #minimize the window size

#driver.delete_all_cookies()    #delete the cookies
#driver.refresh()


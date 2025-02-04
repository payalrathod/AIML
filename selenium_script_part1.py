from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://www.google.com/")

print(driver.title)  # prints the title of the page
print(driver.current_url)  # prints the url of the page
# print(driver.page_source)      prints the html code of the page
# driver.close()  # closes the page

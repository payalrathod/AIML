import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#basic commands

driver = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)             #prints the title of the page
print(driver.current_url)       #prints the url of the page
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click() #do not use elementsbyxpath as it will not have click attribute
#//*[@id="Tabbed"]/a/button use single quotes

# time.sleep(5)
# driver.close()             #     closes only one page
#to close all pages use quit
# driver.quit()



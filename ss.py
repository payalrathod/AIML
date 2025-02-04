import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("http://inlnqw1661:29205/shop")
driver.maximize_window()

a = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[1]/div[2]/div/a/img").click()
b = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[3]/div[2]/div/div/div/div/div/div/div/div/section/div/section/div/ul/li[1]/div/div[4]/button").click()
time.sleep(5)
c = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[3]/div[2]/div/div/div/div/div/div[2]/section/div[2]/div/div/ul/li[1]/div/div[1]/figure/div/img").click()

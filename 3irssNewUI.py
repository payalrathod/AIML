import time
# from select import select

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import unittest
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
import time
# from datetime import datetime

import openpyxl



# driver = webdriver.Chrome(executable_path="C:\\Users\\payalrat\\Downloads\\pc\\chromedriver.exe")

path1 = r'C:\Users\payalrat\PycharmProjects\html\SSURL.xlsx'
wb1 = openpyxl.load_workbook(path1) # this will open your excel file
ws1 = wb1.worksheets[0] # this will open your excel sheet1
LastRowCount = ws1.max_row # this will find max row from the excel

print(LastRowCount)


# driver.get("http://inlnqw1658:29205/shop/menu.html")
# driver.maximize_window()
# time.sleep(3)
# # postpaid plan
# driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[1]/div[2]/div/a/img").click()
# time.sleep(6)
# # select plan
# driver.find_element_by_xpath('//*[@id="btn"]').click()
# time.sleep(20)
# # Continue
# driver.find_element_by_xpath('//*[@id="btn"]').click()
# time.sleep(20)
# # device
# driver.find_element_by_xpath('/html/body/section/div[1]/div[4]/div[3]/div[2]/div/div/div/div/div/div[4]/section/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/img').click()
# # driver.find_elements_by_css_selector('img[src="http://inlnqw1832:29205/content/dam/digitalexp/commerce/catalog/devices/51992-s.png"]').click()
# time.sleep(5)
#
# # add on continue
# # driver.find_element_by_css_selector('button.ds-btn.ds-btn--primary').click()
# # driver.find_element_by_link_text('Continue').click()
# # driver.find_element_by_class_name('ds-btn.ds-btn--primary').click
# # Samsung Galaxy A13 4G
# driver.find_element_by_xpath('/html/body/section/div[1]/div[4]/div[3]/div[2]/div/div/div/div/div/div[4]/section/div[3]/div[1]/div[1]/div[7]/div/div[1]/div[2]').click()
# time.sleep(45)
# # driver.implicitly_wait(10)
#
# # with addon
# # driver.find_element_by_xpath('/html/body/section/div[1]/div[4]/div[2]/div[1]/div[1]/div/section/fieldset[1]/div[2]/div[1]/section/div/div/ul/li/div/div[2]/button[1]').click()
# # without addon
# # driver.find_element_by_xpath('/html/body/section/div[2]/div/div/div/button/span').click()
# # a = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "Continue")))
# # a.click()
# # a = driver.find_element_by_partial_link_text('Conti')
# # a.click()
# button = driver.find_element_by_class_name("/html/body/section/div[1]/div[4]/div/div/div/div/div/div/section/div[1]/div/div/div[2]/div[2]/div[2]/div/section/div/button/span")
# # ds-btn ds-btn--primary ds-btn--bottom-marged
# button.click()
#
# time.sleep(20)
# driver.find_element_by_xpath('/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/div/div/div[2]/div/label[2]/span[1]').click()
# time.sleep(5)
# driver.find_element_by_xpath('/html/body/section/div[2]/div/div/div/button/span').click()
#
# time.sleep(10)
# # checkout now
# driver.find_element_by_xpath('/html/body/section/div[1]/div[4]/div/div/div/section/div[4]/div[2]/div/button/span').click()
# # a = driver.find_element_by_partial_link_text('Chec')
# # a.click()
#
# time.sleep(20)
# # Personal details
# log = driver.find_element_by_name("owningIndividual.firstName")
# log.send_keys("abc")
#
# log = driver.find_element_by_name("owningIndividual.lastName")
# log.send_keys("def")
#
# log = driver.find_element_by_name("date")
# log.send_keys("02")
#
# log1 = driver.find_element_by_name("months")
# log1.send_keys("02")
#
# log2 = driver.find_element_by_name("years")
# log2.send_keys("2000")
#
# field0 = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/section[1]/fieldset/div/div[4]/div/select")
# field0.send_keys("Owner")
# # xpath:
# # /html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/section[1]/fieldset/div/div[4]/div/select
# # dropdown1 = select(driver.find_element_by_name('owningIndividual.residenceStatus'))
# # dropdown1.select_by_visible_text('Owner')
# # select = select(driver.find_element_by_name('owningIndividual.residenceStatus'))
# # select.select_by_value('Owner')
# # dropdown = select(driver.fin_element_by_name('owningIndividual.residenceStatus'))
# # dropdown.select_by_index(2)
#
# log = driver.find_element_by_name("owningIndividual.phone.phoneNumber")
# log.send_keys("0861231213")
#
# log = driver.find_element_by_name("owningIndividual.email.emailAddress")
# log.send_keys("mail123@mail.com")
#
# field0 = driver.find_element_by_name("owningIndividual.identification.identificationType")
# field0.send_keys("Driving Licence")
#
# field0 = driver.find_element_by_name("owningIndividual.addressProof")
# field0.send_keys("Electric Bill")
#
# field0 = driver.find_element_by_name("owningIndividual.employmentCategory")
# field0.send_keys("Management")
#
# field0 = driver.find_element_by_name("owningIndividual.employmentTitle")
# field0.send_keys("General Manager")
#
# log = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/section[3]/fieldset/div/div[3]/div[1]/div[1]/input")
# log.send_keys("05")
#
# log = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/section[3]/fieldset/div/div[3]/div[1]/div[2]/input")
# log.send_keys("2000")
#
# log = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/section[4]/fieldset/div/div/div[1]/div[1]/input")
# log.send_keys("08")
#
# log = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/section[4]/fieldset/div/div/div[1]/div[2]/input")
# log.send_keys("2000")
#
# log = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/fieldset/div/div[1]/div[2]/div[1]/div[1]/input")
# log.send_keys("12")
#
# log = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/fieldset/div/div[1]/div[2]/div[1]/div[2]/input")
# log.send_keys("2000")
#
# log = driver.find_element_by_name('address.addressLine1')
# log.send_keys('789 Ballyhade, Castledermot, Co. Kildare')
#
# time.sleep(4)
#
# log = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[2]/div[1]/div/div/section/div/div/fieldset/div/section/div[2]/fieldset/div/div[1]/div/div[2]/ul/li/div")
# log.click()
#
# time.sleep(3)
#
# a = driver.find_element_by_xpath("/html/body/section/div[2]/div/div[2]/div/button/span")
# a.click()
#
# time.sleep(5)
#
# # delivery method screen
# # a = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[3]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/fieldset/div/div[2]/div/input")
# # a.send_keys("AIBKIE2DXXX")
# # log = driver.find_element_by_name("bankCode")
# # log.send_keys("AIBKIE2DXXX")
#
# # Pay by card
# # driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[3]/div[1]/div[3]/div/div/div/div[2]/div/div/ul/li[2]/label/span[2]").click()
#
# time.sleep(60)
#
# # a = driver.find_element_by_xpath("/html/body/section/div[1]/div[4]/div[3]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div[1]/div/fieldset/div/div[3]/div/input")
# # a.send_keys("IE24AIBK93247730722084")
# # log = driver.find_element_by_name("accountNumber")
# # log.send_keys("IE24AIBK93247730722084")
#
# inputbox = driver.find_elements(By.XPATH, '//*[@id="bankCode"]')
# driver.find_element(By.ID, 'bankCode').send_keys('AIBKIE2DXXX')
# # inputbox.send_keys('AIBKIE2DXXX')
# # print(len(inputbox))
#
# time.sleep(3)
#
# driver.find_element(By.ID, 'accountNumber').send_keys('IE24AIBK93247730722084')
#
# time.sleep(3)
# # driver.find_element_by_xpath('/html/body/section/div[1]/div[4]/div[3]/div[1]/div[3]/div/div/div/section/div[2]/div/label/div/span[2]')
# # a.click()
# driver.find_element(By.CLASS_NAME, 'ds-off').click()
#
# time.sleep(5)
#
# a = driver.find_element_by_xpath("/html/body/section/div[2]/div/div[2]/div/button/span")
# a.click()
#
# time.sleep(50)
#
# # to take SS of page
# # driver.get_screenshot_as_file("screenshot.png")
#
# # element = driver.find_element_by_tag_name('span')
# # # Get Text
# # print(element.text)
#
# driver.find_element(By.XPATH, '/html/body/section/div[1]/div[4]/div/div/div/section/section/div[2]/div[7]/form/fieldset/div/div/div[1]/label/div/span[2]').click()
#
# # login_form = driver.find_element_by_tag_name('span')
# # print(login_form)
#
# time.sleep(10)
#
# driver.find_element(By.XPATH, '/html/body/section/div[1]/div[4]/div/div/div/section/section/footer/button/span').click()
#
# time.sleep(30)
#
# driver.find_element(By.ID, 'cardNumber').send_keys('5555555555554444')
# driver.find_element(By.ID, 'cardholderName').send_keys('abc')
# driver.find_element(By.ID, 'expiryMonth').send_keys('01')
# driver.find_element(By.ID, 'expiryYear').send_keys('30')
# driver.find_element(By.ID, 'securityCode').send_keys('203')
#
# time.sleep(5)
#
# driver.find_element(By.ID, 'submitButton').click()
#
#
#
#

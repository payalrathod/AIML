from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\Users\\payalrat\\Downloads\\pc\\chromedriver.exe")

driver.get("http:inlnqw1859:34000/retail/#")

log = driver.find_element_by_name("userID")
log1 = driver.find_element_by_name("password")
log2 = driver.find_element_by_name("storeId")

log.send_keys("posuser")
log1.send_keys("Amdocs12345!")
log2.send_keys("312")

driver.find_element_by_css_selector('.ds-btn.ds-btn--primary').click()
driver.maximize_window()

# driver.find_element_by_css_selector("number").send_keys("0860895842")
#driver.find_element_by_link_text("Account Number").click()
#log3 = driver.find_element_by_name("accountNumberInputField")
#log3.send_keys("287488472")
#driver.find_elements_by_xpath("//*[@id='main']/div/main/div[3]/section/div[1]/div/div/button/span").click()
#driver.find_elements_by_class_name('ds-filter-combined__action').click()

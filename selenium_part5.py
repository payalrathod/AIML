from selenium import webdriver
from selenium.webdriver.common.keys import Keys

c = webdriver.Chrome(executable_path="C:/Users/payalrat/Downloads/chromedriver/chromedriver-win64/chromedriver.exe")
c.get('https://www.google.com/')
print(c.title)

b = c.find_element_by_class_name("gLFyf")
v = b.send_keys("Steve Jobs")
x = b.send_keys(Keys.ENTER)

if c.find_elements_by_link_text("https://en.wikipedia.org/"):
    print(True)
# else:
    # c.close()
# if c.find_element_by_class_name("https://www.wikipedia.org/").get_attribute("wikipedia").is_displayed():
#     print(True)
# else:
#     print(False)

#a = print(c.find_element_by_class_name("LC20lb.MBeuO.DKV0Md").is_displayed())
    #.get_attribute("Wikipedia")




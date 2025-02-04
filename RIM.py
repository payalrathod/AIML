import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/payalrat/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_RIM(self):
        self.driver.get("http://inlnqw1376:34000/retail#/")
        self.driver.find_element_by_name("userID").send_keys("posuser")
        self.driver.find_element_by_name("password").send_keys("America1!")
        self.driver.find_element_by_xpath("/html/body/div/div/main/div[3]/section/div/div/div[2]/form/button/span").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed!')


if __name__ == '__main__':
    unittest.main()

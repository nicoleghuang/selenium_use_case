#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re
import HTMLTestRunner

now=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
#print now

class Baidua(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com/"
        self.verificationError=[]
        self.accept_next_alert=True

    def test_baidua_search(self):
        u"百度搜索用例"
        driver=self.driver
        driver.get(self.base_url+"/")
        try:
            driver.find_element_by_id("kw").send_keys("viabtc")
        except:
            driver.get_screenshot_as_file('D:\\selenium_use_case\\error_png\\' + now + '.png')
        driver.find_element_by_id("su").click()
        time.sleep(5)

        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationError)

if __name__=="__main__":
    #HTMLTestRunner.main()
    #unittest.main()
    testsuite=unittest.TestSuite
    testsuite.addTest(Baidua("test_baidua_search"))
    result=unittest.TextTestRunner().run(testsuite)
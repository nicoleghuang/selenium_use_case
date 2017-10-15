#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest
import time,re

class Sogo(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.sogo.com/"
        self.error=[]
        self.accept_next_alert=True

    def test_sogo_search(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_xpath('//*[@id="query"]').send_keys("2017/11/15")
        now=time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())
        try:
            driver.find_element_by_xpath('//*[@id="tb"]').click()
        except:
            driver.save_screenshot("D:\\selenium_use_case\\error_png\\"+now+"_sogo.png")
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.error)

if __name__=="__main__":

    suite=unittest.TestSuite()
    suite.addTest(Sogo("test_sogo_search"))
    result=unittest.TextTestRunner.run(suite)





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

class YouDao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.youdao.com/"
        self.verificationError=[]
        self.accept_next_alert = True

    def test_youdao_search(self):
        u"""有道搜索用例"""
        driver=self.driver
        driver.get(self.base_url+"/")
        try:
            driver.find_element_by_id("qw").send_keys("viabtc")
            driver.find_element_by_id("query").click()
            time.sleep(5)
        except:
            driver.get_screenshot_as_file('D:\\selenium_use_case\\error_png\\'+now+'.png')
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationError)

if __name__=="__main__":
    #HTMLTestRunner.main()
    #unittest.main()
    testsuite=unittest.TestSuite
    testsuite.addTest(YouDao("test_youdao_search"))
    unittest.TextTestRunner().run(testsuite)

#filename='D:\\selenium_use_case\\report\\'+now+'_result.html'
#fp=file(filename,'wb')
#runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="test_report",description="this is the description of this report")
#runner.run(testsuite)

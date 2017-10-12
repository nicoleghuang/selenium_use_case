#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time,unittest,re
import HTMLTestRunner

class Baidoo(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com/"
        self.verificationErrors=[]
        self.accept_next_alert=True

    def test_search(self):
        driver=self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        driver.close()

    def test_set(self):
        driver=self.driver
        driver.get(self.base_url+'/gaoji/preferences.html')
        m=driver.find_element_by_name("NR")
        m.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def test_searchSecond(self):
        driver=self.driver
        driver.get(self.base_url+'/')
        now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        pic_path="D:\\selenium_use_case\\report\\image\\"+now+"_kw.png"
        print pic_path
        try:
            driver.find_element_by_id("kwww").send_keys("hello")
        except:
            #driver.get_screenshot_as_file(pic_path)
            driver.save_screenshot(pic_path)
            time.sleep(2)
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "main":
    HTMLTestRunner.main()

testunit = unittest.TestSuite()
#testunit.addTest(Baidoo("test_search"))
#testunit.addTest(Baidoo("test_set"))
testunit.addTest(Baidoo("test_searchSecond"))

now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
filename = 'D:\\selenium_use_case\\report\\'+now+'_result.html'
fp = file(filename,"wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="Report_title", description="Report_description" )
runner.run(testunit)
#runner.run(Baidoo("test_search"))
#runner.run(Baidoo("test_set"))
#runner.run(Baidoo("test_searchSecond"))


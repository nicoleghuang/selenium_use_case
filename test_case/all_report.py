#coding=utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import sys
sys.path.append("D:/selenium_use_case/test_case")
from untie import *
#from demo import test_baidu,test_youdao

import unittest,doctest
import HTMLTestRunner
import time,os

suite = doctest.DocTestSuite()
suite.addTest(unittest.makeSuite(test_youdao.YouDao))
suite.addTest(unittest.makeSuite(test_baidu.Baidua))
suite.addTest(unittest.makeSuite(test_sogo.Sogo))

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
filename = 'D:\\selenium_use_case\\report\\'+now+'_result.html'
fp = file(filename,"wb")

runner = HTMLTestRunner.HTMLTestRunner( stream=fp,title="my_report_title",description="this is the description")

runner.run(suite)

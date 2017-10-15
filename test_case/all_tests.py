#coding=utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import unittest,doctest
import sys
sys.path.append("D:\\selenium_use_case\\test_case\\untie")
#from demo import test_youdao,test_baidu
#from untie import test_youdao,test_baidu
from untie import *

import HTMLTestRunner


suite=doctest.DocTestSuite()
#list the files will be executed
suite.addTest(unittest.makeSuite(test_youdao.YouDao))
suite.addTest(unittest.makeSuite(test_baidu.Baidua))

unittest.TextTestRunner(verbosity=2).run(suite)

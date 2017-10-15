#coding=utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import sys,re,os,math
sys.path.append("D:/selenium_use_case/test_case")
from untie import *
from untie.sogou import *
#print "success"
import unittest,doctest,site,time
import HTMLTestRunner
#allTestName=["untie.test_baidu.Baidu","untie.test_youdao.Youdao","untie.sogo.test_sogo.Sogo"]
allTestName=["untie.test_baidu","untie.test_youdao","untie.test_sogo"]

suite=unittest.TestSuite()

#suite.addTest(unittest.defaultTestLoader.loadTestsFromName("untie.test_sogo"))

if __name__=="__main__":
    for test in allTestName:
        print test
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print "Skipping test from '%s'" % test
            try:
                __import__(test)
            except ImportError:
                print "Can not import the test module!"
            else:
                print "Can not load the test suite!"
            from traceback import print_exc
        print
        print "Running the tests....."


now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
filename="D:\\selenium_use_case\\report\\"
fp=file(filename+now+"_result.html","wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="report_result",description="report_description")
runner.run(suite)
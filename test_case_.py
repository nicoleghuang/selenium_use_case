#coding=utf-8
import os
caselist=os.listdir('D:\\selenium_use_case\\test_case')
for a in caselist:
    s=a.split('.')[1:][0]  #choose case which will be executed
    if s=='py':
        os.system('"C:\Python27\python.exe" D:\\selenium_use_case\\test_case\\%s 1>>log.txt 2>&1'%a)






'''
Created on Jul 31, 2019

@author: tfu
'''
from bs4 import BeautifulSoup
import re

def getReportName(html):
    soup=BeautifulSoup(html,"html.parser")
    reportName=soup.find('div',id="infos").h1.text
    cutName=re.search(r'/| .+', reportName)
    cutName=cutName.group(0)[3:]
    return cutName
    
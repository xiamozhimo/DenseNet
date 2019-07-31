'''
Created on Jul 31, 2019

@author: tfu
'''
import requests
from bs4 import BeautifulSoup
from werkzeug import urls
import os
import re
from indextool.indexhtml import getHtml,getHtml,getHtmlUrl,getjumplink

def getReportName(html):
    soup=BeautifulSoup(html,"html.parser")
    reportName=soup.find('div',id="infos").h1.text
    cutName=re.search(r'/| .+', reportName)
    cutName=cutName.group(0)[3:]
    return cutName
    
def savePics(pageList):
    for pagelink in pageList:
        html=getHtml(pagelink)
        soup=BeautifulSoup(html,"html.parser")
        reportName=getReportName(html)
        i=1
        all_img=soup.find('div',class_='content-container').find_all('img')    
        for img in all_img:
            src=img['src']
            print(src)
            root='D:/wormgetpic/'
            path=root + reportName + str(i) +'.jpg'
            i=i+1
            try:
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r= requests.get(src)
                    with open(path,'wb') as f:
                        f.write(r.content)
                    print('Success')   
                else:
                    print('Already Exist')       
            except Exception as e:
                print(e)
'''
Created on Jul 31, 2019

@author: tfu
'''
import requests
from bs4 import BeautifulSoup
import os
from indextool.indexhtml import getHtml
from subpagetool.subpagehtml import getReportName

def makeFolderPath(root,reportName):
    folderpath=root+reportName +'/'       
    return folderpath

def makeFilePath(forlderpath,reportName,i):
    filepath=forlderpath+reportName+str(i)+'.jpg'
    return filepath
    
    
def checkmakefolder(root):
    if not os.path.exists(root):
        os.mkdir(root)
        print("Folder Created: ",root)


def savePics(pageList,root,contidueMode=0,startPoint=0,endPoint=9999):
    checkmakefolder(root)
    if contidueMode==1:
        pageList=pageList[startPoint:endPoint]
    for pagelink in pageList:
        html=getHtml(pagelink)
        soup=BeautifulSoup(html,"html.parser")
        reportName=getReportName(html).replace(r'/',' ')
        i=1
        all_img=soup.find('div',class_='content-container').find_all('img')    
        forlderpath=makeFolderPath(root, reportName)
        for img in all_img:
            checkmakefolder(forlderpath)
            filepath=makeFilePath(forlderpath,reportName,i)
            src=img['src']
            print('Processing:',src)
            i=i+1
            try:
                if not os.path.exists(filepath):
                    r= requests.get(src)
                    with open(filepath,'wb') as f:
                        f.write(r.content)
                    print('Success, filepath:',filepath)   
                else:
                    print('File %s is already exist' %filepath)       
            except Exception as e:
                print(e)
'''
Created on Jul 29, 2019

@author: tfu
'''
import requests
from bs4 import BeautifulSoup
from werkzeug import urls
import os

url='https://www.woodenears.com/list?category=5b6171cf823aea488f19e1d0&name=%E8%80%B3%E6%9C%BA%E6%B5%8B%E9%87%8F%E6%8A%A5%E5%91%8A'
baseJumpRoot='https://www.woodenears.com'


def getPageRange(url):    
    pageRange=[]    
    r= requests.get(url)
    r.raise_for_status()
    r.encoding= r.apparent_encoding
    html=r.text
    soup=BeautifulSoup(html,"html.parser")
    numbers = soup.find('ul',class_="el-pager").find_all('li')
    for number in numbers:
        pageRange.append(number.text)
    return pageRange

    
    

def getHtmlUrl(url,pageRange):
    indexList=[]
    for i in pageRange:
        urljump=url+'&pageIndex='+i
        r= requests.get(urljump)
        r.raise_for_status()
        r.encoding= r.apparent_encoding
        indexList.append(r.text)
    return indexList

def getjumplink(baseJumpRoot,indexList):
    pageList=[]
    for html in indexList:
        soup=BeautifulSoup(html,"html.parser")
        links=soup.find('div',id="listContent").find_all('a')
        for link in links:
            pageList.append(baseJumpRoot+link['href'])
    return pageList



pageRange=getPageRange(url)
indexList=getHtmlUrl(url,pageRange)
pageList = getjumplink(baseJumpRoot,indexList)
print(pageList)

